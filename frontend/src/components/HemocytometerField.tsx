import { useState } from "react";
import type { BenchAction, BenchRun } from "../types";

export type CellDecision = "unstained" | "stained" | "exclude";
export interface ChamberCell {
  id: string;
  x: number;
  y: number;
  stained: boolean;
  decision: CellDecision | null;
}

const cellPattern =
  /([AB]-\d+) at x=([\d.]+), y=([\d.]+); (stained|unstained); decision: (pending|unstained|stained|exclude)/g;

export function chamberCells(run: BenchRun): ChamberCell[] {
  const panel = run.panels.find((item) =>
    item.title.startsWith("Microscope field:"),
  );
  const field = panel?.rows.find(([label]) => label === "Visible cells")?.[1];
  if (!field) return [];
  return [...field.matchAll(cellPattern)].map((match) => ({
    id: match[1],
    x: Number(match[2]),
    y: Number(match[3]),
    stained: match[4] === "stained",
    decision: match[5] === "pending" ? null : (match[5] as CellDecision),
  }));
}

export function tallyCells(cells: ChamberCell[]) {
  return {
    unstained: cells.filter((cell) => cell.decision === "unstained").length,
    stained: cells.filter((cell) => cell.decision === "stained").length,
    excluded: cells.filter((cell) => cell.decision === "exclude").length,
  };
}

export default function HemocytometerField({
  run,
  busy,
  onAct,
}: {
  run: BenchRun;
  busy: boolean;
  onAct: (action: BenchAction) => void;
}) {
  const cells = chamberCells(run);
  const [selected, setSelected] = useState<string | null>(null);
  const chamber = run.panels
    .find((panel) => panel.title.startsWith("Microscope field:"))
    ?.title.slice(-1);
  const tally = tallyCells(cells);
  const selectedCell = cells.find((cell) => cell.id === selected);

  function classify(classification: CellDecision) {
    if (!selectedCell) return;
    onAct({
      name: "mark_cell",
      params: { cell_id: selectedCell.id, classification },
    });
  }

  if (!cells.length || !chamber) return null;
  return (
    <section
      className="card hemocytometer"
      aria-labelledby="hemocytometer-title"
    >
      <h3 id="hemocytometer-title">
        Interactive counting field · chamber {chamber}
      </h3>
      <p>
        Select a cell, then classify it. Include top/left boundary cells;
        exclude bottom/right. Stain and boundary decisions are separate.
      </p>
      <div className="tabs" aria-label="Loaded counting chambers">
        {["A", "B"].map((name) => {
          const loaded = run.panels.some((panel) =>
            panel.rows.some(
              ([label, value]) =>
                label === "Chambers loaded" && value.includes(name),
            ),
          );
          return loaded ? (
            <button
              key={name}
              aria-current={chamber === name ? "page" : undefined}
              disabled={busy}
              onClick={() => {
                setSelected(null);
                onAct({ name: "select_chamber", params: { chamber: name } });
              }}
            >
              Chamber {name}
            </button>
          ) : null;
        })}
      </div>
      <div className="hemocytometer-layout">
        <svg
          className="hemocytometer-grid"
          viewBox="-0.06 -0.06 1.12 1.12"
          role="group"
          aria-label={`Chamber ${chamber} synthetic cell field`}
        >
          <rect
            x="0"
            y="0"
            width="1"
            height="1"
            className="chamber-background"
          />
          {[1, 2].map((line) => (
            <g key={line}>
              <line
                x1={line / 3}
                y1="0"
                x2={line / 3}
                y2="1"
                className="chamber-line"
              />
              <line
                x1="0"
                y1={line / 3}
                x2="1"
                y2={line / 3}
                className="chamber-line"
              />
            </g>
          ))}
          <path d="M 0 1 L 0 0 L 1 0" className="chamber-include" />
          <path d="M 1 0 L 1 1 L 0 1" className="chamber-exclude" />
          {cells.map((cell) => (
            <g
              key={cell.id}
              role="button"
              tabIndex={0}
              aria-label={`Cell ${cell.id}, ${cell.stained ? "stained" : "unstained"}, ${cell.decision || "not classified"}`}
              aria-pressed={selected === cell.id}
              className={`chamber-cell ${cell.stained ? "cell-stained" : "cell-unstained"} ${cell.decision ? `cell-${cell.decision}` : ""}`}
              transform={`translate(${cell.x} ${cell.y})`}
              onClick={() => setSelected(cell.id)}
              onKeyDown={(event) => {
                if (event.key === "Enter" || event.key === " ") {
                  event.preventDefault();
                  setSelected(cell.id);
                }
              }}
            >
              <circle r="0.025" />
              <text y="0.009">{cell.id.split("-")[1]}</text>
            </g>
          ))}
        </svg>
        <div>
          <p aria-live="polite">
            <strong>
              {selectedCell ? `Cell ${selectedCell.id}` : "No cell selected"}
            </strong>
            <br />
            {tally.unstained} unstained · {tally.stained} stained ·{" "}
            {tally.excluded} excluded
          </p>
          <div className="cell-decisions" aria-label="Cell classification">
            <button
              disabled={busy || !selectedCell}
              onClick={() => classify("unstained")}
            >
              Include unstained
            </button>
            <button
              disabled={busy || !selectedCell}
              onClick={() => classify("stained")}
            >
              Include stained
            </button>
            <button
              disabled={busy || !selectedCell}
              onClick={() => classify("exclude")}
            >
              Exclude boundary
            </button>
          </div>
        </div>
      </div>
      <details className="cell-text-list">
        <summary>Text list of cells and classifications</summary>
        <ul>
          {cells.map((cell) => (
            <li key={cell.id}>
              {cell.id}: x={cell.x}, y={cell.y};{" "}
              {cell.stained ? "stained" : "unstained"};{" "}
              {cell.decision || "pending"}{" "}
              <button
                aria-label={`Select cell ${cell.id} from text list`}
                aria-pressed={selected === cell.id}
                onClick={() => setSelected(cell.id)}
              >
                Select
              </button>
            </li>
          ))}
        </ul>
      </details>
      <p className="muted">
        Synthetic diagram, not a microscope image. It teaches counting
        decisions, not focus, morphology recognition or physical technique.
      </p>
    </section>
  );
}
