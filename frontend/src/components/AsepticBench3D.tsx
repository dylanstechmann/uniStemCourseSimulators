import {
  Component,
  Suspense,
  useEffect,
  useState,
  type ReactNode,
} from "react";
import { Canvas, useThree } from "@react-three/fiber";
import { ContactShadows, Html, OrbitControls } from "@react-three/drei";
import type { BenchRun } from "../types";

type Panels = BenchRun["panels"];
type ItemKind = "flask" | "bottle" | "waste" | "supplies" | "unknown";

const ITEM_KINDS: Record<string, ItemKind> = {
  "target culture flask": "flask",
  "turbid culture flask": "flask",
  "second cell-line flask": "flask",
  "fresh-medium lot A": "bottle",
  "fresh-medium lot B": "bottle",
  "spent-medium waste container": "waste",
  "sterile single-use pipettes": "supplies",
  "pipette aid": "supplies",
  "sterility-test broth tubes": "supplies",
  "penicillin-streptomycin stock": "bottle",
};

const CULTURE_LABELS: Record<string, string> = {
  "target culture flask": "Target flask",
  "turbid culture flask": "Turbid flask",
};

function rowsFor(panels: Panels, title: string) {
  return panels.find((panel) => panel.title === title)?.rows ?? [];
}

function valueFor(rows: [string, string][], label: string) {
  return rows.find(([name]) => name === label)?.[1] ?? "";
}

export function asepticSceneState(panels: Panels) {
  const cabinetRows = rowsFor(panels, "Cabinet");
  const cultureRows = rowsFor(panels, "Culture");
  const openRows = rowsFor(panels, "Open containers");
  const openContainers = new Map(openRows);
  const items = rowsFor(panels, "Inside the cabinet")
    .filter(([name, placement]) => !(name === "—" && placement === "empty"))
    .map(([name, placement]) => {
      const [zone = "", ...flags] = placement
        .split(",")
        .map((part) => part.trim());
      const cultureLabel = CULTURE_LABELS[name];
      return {
        name,
        kind: ITEM_KINDS[name] ?? ("unknown" as const),
        zone: zone || "not reported",
        placement,
        notWiped: flags.includes("not wiped"),
        open: openContainers.has(name),
        closure: openContainers.get(name) ?? "",
        appearance: cultureLabel ? valueFor(cultureRows, cultureLabel) : "",
      };
    });
  const visiblePanels = panels
    .map(
      (panel) =>
        `${panel.title}: ${panel.rows
          .map(([label, value]) => `${label} — ${value}`)
          .join("; ")}`,
    )
    .join(". ");
  const description = `Procedural cabinet illustration, not to scale. The clean side is on the left, the work center is in the middle and the dirty side is on the right. The cabinet work zone, front opening, front grille and rear grille are labelled. Loaded items, closures and readings come only from the visible panels. ${
    visiblePanels || "No visible panel rows were supplied."
  }`;
  return {
    cabinet: {
      criticalZone: valueFor(cabinetRows, "Critical zone"),
      interior: valueFor(cabinetRows, "Interior"),
      uvLamp: valueFor(cabinetRows, "UV lamp"),
      openFlame: valueFor(cabinetRows, "Open flame"),
    },
    culture: {
      spentMedium: valueFor(cultureRows, "Spent medium removed"),
      freshMedium: valueFor(cultureRows, "Fresh medium added"),
    },
    items,
    description,
  };
}

type SceneState = ReturnType<typeof asepticSceneState>;
type SceneItem = SceneState["items"][number];
type Position = [number, number, number];

function Label({
  children,
  position,
}: {
  children: ReactNode;
  position: Position;
}) {
  return (
    <Html
      position={position}
      center
      className="bench-3d-label"
      distanceFactor={10}
    >
      {children}
    </Html>
  );
}

function Cabinet({ state }: { state: SceneState }) {
  const zones = [
    { name: "Clean side", x: -2.85, color: "#cfe4d4" },
    { name: "Work center", x: 0, color: "#d6e2e8" },
    { name: "Dirty side", x: 2.85, color: "#ead5c9" },
  ];
  return (
    <group>
      <mesh position={[0, 2.1, -1.85]} receiveShadow>
        <boxGeometry args={[9.2, 4.2, 0.16]} />
        <meshStandardMaterial color="#dbe4e2" roughness={0.7} />
      </mesh>
      {[-4.52, 4.52].map((x) => (
        <mesh key={x} position={[x, 2.1, 0]} receiveShadow>
          <boxGeometry args={[0.16, 4.2, 3.8]} />
          <meshStandardMaterial color="#c7d2d0" roughness={0.65} />
        </mesh>
      ))}
      <mesh position={[0, 4.15, 0]} castShadow>
        <boxGeometry args={[9.2, 0.22, 3.85]} />
        <meshStandardMaterial color="#aebfbc" roughness={0.55} />
      </mesh>
      <mesh position={[0, 3.85, 1.86]} castShadow>
        <boxGeometry args={[9.2, 0.55, 0.16]} />
        <meshStandardMaterial color="#8fa5a1" roughness={0.5} />
      </mesh>
      <Label position={[0, 3.85, 2.02]}>Front opening · keep clear</Label>
      <Label position={[0, 3.15, -1.65]}>
        Cabinet interior · {state.cabinet.interior || "not reported"}
      </Label>
      <Label position={[0, 2.55, -1.65]}>
        Work zone ·{" "}
        {state.cabinet.criticalZone || "classification not reported"}
      </Label>
      <Label position={[0, 1.95, -1.65]}>
        UV lamp · {state.cabinet.uvLamp || "not reported"}
      </Label>
      {zones.map((zone) => (
        <group key={zone.name}>
          <mesh position={[zone.x, 0.02, 0]} receiveShadow>
            <boxGeometry args={[2.75, 0.04, 2.6]} />
            <meshStandardMaterial color={zone.color} roughness={0.8} />
          </mesh>
          <Label position={[zone.x, 0.22, 0.95]}>{zone.name}</Label>
        </group>
      ))}
      {[-1.25, 1.25].map((z) => (
        <group key={z}>
          {Array.from({ length: 15 }, (_, index) => (
            <mesh key={index} position={[-3.5 + index * 0.5, 0.075, z]}>
              <boxGeometry args={[0.32, 0.025, 0.28]} />
              <meshStandardMaterial color="#617672" roughness={0.6} />
            </mesh>
          ))}
          <Label position={[0, 0.32, z]}>
            {z > 0 ? "Front grille" : "Rear grille"} · keep clear
          </Label>
        </group>
      ))}
      {state.cabinet.openFlame && (
        <group position={[3.7, 0.3, -0.7]}>
          <mesh>
            <coneGeometry args={[0.18, 0.65, 20]} />
            <meshStandardMaterial color="#e88438" emissive="#8a2e0d" />
          </mesh>
          <Label position={[0, 0.75, 0]}>
            Open flame · {state.cabinet.openFlame}
          </Label>
        </group>
      )}
    </group>
  );
}

function Closure({ item, height }: { item: SceneItem; height: number }) {
  if (!item.open) {
    return (
      <mesh position={[0, height, 0]} castShadow>
        <cylinderGeometry args={[0.24, 0.24, 0.16, 24]} />
        <meshStandardMaterial color="#527a71" roughness={0.4} />
      </mesh>
    );
  }
  const position: Position = item.closure.includes("held above")
    ? [0, height + 0.45, 0]
    : [0.58, 0.12, 0];
  return (
    <>
      <mesh position={[0, height - 0.08, 0]}>
        <cylinderGeometry args={[0.2, 0.2, 0.05, 24]} />
        <meshStandardMaterial color="#263f3a" />
      </mesh>
      <mesh
        position={position}
        rotation={
          item.closure.includes("face down") ? [Math.PI, 0, 0] : [0, 0, 0]
        }
        castShadow
      >
        <cylinderGeometry args={[0.24, 0.24, 0.16, 24]} />
        <meshStandardMaterial color="#527a71" roughness={0.4} />
      </mesh>
    </>
  );
}

function Vessel({ item }: { item: SceneItem }) {
  const flask = item.kind === "flask";
  const waste = item.kind === "waste";
  const height = waste ? 1.25 : flask ? 0.75 : 1.05;
  const liquidColor = item.appearance.includes("turbid")
    ? "#ad8851"
    : item.appearance.includes("clear")
      ? "#d9b1a6"
      : "#d7cc8c";
  return (
    <group>
      <mesh position={[0, height / 2, 0]} castShadow>
        {flask ? (
          <boxGeometry args={[0.85, height, 0.58]} />
        ) : (
          <cylinderGeometry
            args={[waste ? 0.48 : 0.36, waste ? 0.52 : 0.4, height, 28]}
          />
        )}
        <meshStandardMaterial
          color={waste ? "#adb8b5" : "#e1eeee"}
          transparent
          opacity={0.78}
          roughness={0.25}
        />
      </mesh>
      {!waste && (
        <mesh position={[0, height * 0.35, 0]}>
          {flask ? (
            <boxGeometry args={[0.72, height * 0.35, 0.48]} />
          ) : (
            <cylinderGeometry args={[0.31, 0.34, height * 0.45, 24]} />
          )}
          <meshStandardMaterial color={liquidColor} transparent opacity={0.8} />
        </mesh>
      )}
      <mesh position={[0, height + 0.12, 0]} castShadow>
        <cylinderGeometry args={[0.19, 0.24, 0.3, 24]} />
        <meshStandardMaterial color="#d7e5e3" transparent opacity={0.8} />
      </mesh>
      <Closure item={item} height={height + 0.32} />
    </group>
  );
}

function Supplies({ item }: { item: SceneItem }) {
  if (item.name === "sterile single-use pipettes") {
    return (
      <group>
        <mesh position={[0, 0.12, 0]} castShadow>
          <boxGeometry args={[1.05, 0.24, 0.7]} />
          <meshStandardMaterial color="#6f9488" />
        </mesh>
        {[-0.3, 0, 0.3].map((x) => (
          <mesh key={x} position={[x, 0.45, 0]} rotation={[0, 0, 0.2]}>
            <cylinderGeometry args={[0.035, 0.012, 0.85, 12]} />
            <meshStandardMaterial color="#e3f0ec" />
          </mesh>
        ))}
      </group>
    );
  }
  if (item.name === "sterility-test broth tubes") {
    return (
      <group>
        <mesh position={[0, 0.12, 0]} castShadow>
          <boxGeometry args={[1, 0.24, 0.55]} />
          <meshStandardMaterial color="#78958a" />
        </mesh>
        {[-0.3, 0, 0.3].map((x) => (
          <mesh key={x} position={[x, 0.48, 0]}>
            <cylinderGeometry args={[0.09, 0.07, 0.7, 16]} />
            <meshStandardMaterial color="#e4d89f" transparent opacity={0.85} />
          </mesh>
        ))}
      </group>
    );
  }
  return (
    <group>
      <mesh position={[0, 0.4, 0]} castShadow>
        <cylinderGeometry args={[0.22, 0.27, 0.8, 24]} />
        <meshStandardMaterial color="#5d8c7c" roughness={0.4} />
      </mesh>
      <mesh position={[0, 0.9, 0]}>
        <cylinderGeometry args={[0.08, 0.08, 0.3, 16]} />
        <meshStandardMaterial color="#d9e5e1" />
      </mesh>
    </group>
  );
}

function CabinetItem({
  item,
  position,
}: {
  item: SceneItem;
  position: Position;
}) {
  const vessel =
    item.kind === "flask" || item.kind === "bottle" || item.kind === "waste";
  return (
    <group position={position}>
      {vessel ? (
        <Vessel item={item} />
      ) : item.kind === "supplies" ? (
        <Supplies item={item} />
      ) : (
        <mesh position={[0, 0.4, 0]} castShadow>
          <boxGeometry args={[0.75, 0.8, 0.65]} />
          <meshStandardMaterial color="#b9c5c1" />
        </mesh>
      )}
      <Label position={[0, 1.75, 0]}>
        {item.name}
        {vessel ? ` · ${item.open ? `open; ${item.closure}` : "closed"}` : ""}
        {item.notWiped ? " · not wiped" : ""}
        {item.appearance ? ` · ${item.appearance}` : ""}
      </Label>
      <Label position={[0, -0.18, 0]}>{item.placement}</Label>
    </group>
  );
}

type ZoneSlots = { xs: number[]; zs: number[]; y?: number };

const ZONE_SLOTS: Record<string, ZoneSlots> = {
  "clean side": { xs: [-3.75, -2.6, -1.45], zs: [-0.95, 0.95] },
  "work center": { xs: [0, 0.8, -0.8], zs: [-0.95, 0.15, 1.15] },
  "dirty side": { xs: [1.45, 2.6, 3.75], zs: [-0.95, 0.95] },
  "front opening": { xs: [-3.6, -1.8, 0, 1.8, 3.6], zs: [1.5] },
  "front grille": { xs: [-3.6, -1.8, 0, 1.8, 3.6], zs: [1.15] },
  "rear grille": { xs: [-3.6, -1.8, 0, 1.8, 3.6], zs: [-1.2] },
  stacked: { xs: [0, 0.8, -0.8], zs: [-0.95, 0.15, 1.15], y: 0.3 },
};
const UNKNOWN_ZONE_SLOTS: ZoneSlots = {
  xs: [-3.6, -1.8, 0, 1.8, 3.6],
  zs: [-0.95, 0.95],
};
const MIN_ITEM_DISTANCE = 1.15;

function candidatesForZone(zone: string): Position[] {
  const slots = ZONE_SLOTS[zone] ?? UNKNOWN_ZONE_SLOTS;
  const y = slots.y ?? 0.08;
  return slots.zs.flatMap((z) => slots.xs.map((x) => [x, y, z] as Position));
}

function horizontalDistance(a: Position, b: Position) {
  return Math.hypot(a[0] - b[0], a[2] - b[2]);
}

export function layoutCabinetItems(items: SceneItem[]) {
  const occupied: Position[] = [];
  return items.map((item) => {
    const candidates = candidatesForZone(item.zone);
    const clearance = (candidate: Position) =>
      Math.min(
        ...occupied.map((position) => horizontalDistance(candidate, position)),
      );
    let position = candidates.find((candidate) =>
      occupied.every(
        (other) =>
          horizontalDistance(candidate, other) + 1e-9 >= MIN_ITEM_DISTANCE,
      ),
    );
    if (!position) {
      // Pathological overfull panels stay bounded: use the roomiest known slot.
      position = candidates.reduce((best, candidate) =>
        clearance(candidate) > clearance(best) ? candidate : best,
      );
    }
    occupied.push(position);
    return { item, position };
  });
}

function LoadedItems({ items }: { items: SceneItem[] }) {
  return layoutCabinetItems(items).map(({ item, position }, index) => (
    <CabinetItem
      key={`${item.name}:${index}`}
      item={item}
      position={position}
    />
  ));
}

export type ViewAction =
  "reset" | "zoom-in" | "zoom-out" | "rotate-left" | "rotate-right";

type ViewCommand = { action: ViewAction; revision: number };

const CAMERA_TARGET: Position = [0, 1.25, 0];
const DEFAULT_CAMERA_POSITION: Position = [8, 6.2, 11];
const MIN_CAMERA_DISTANCE = 6;
const MAX_CAMERA_DISTANCE = 20;

export function nextCameraPosition(
  action: ViewAction,
  current: Position = DEFAULT_CAMERA_POSITION,
): Position {
  if (action === "reset") return [...DEFAULT_CAMERA_POSITION];
  if (action === "rotate-left" || action === "rotate-right") {
    const angle = (action === "rotate-left" ? 1 : -1) * (Math.PI / 12);
    const x = current[0] - CAMERA_TARGET[0];
    const z = current[2] - CAMERA_TARGET[2];
    return [
      CAMERA_TARGET[0] + x * Math.cos(angle) - z * Math.sin(angle),
      current[1],
      CAMERA_TARGET[2] + x * Math.sin(angle) + z * Math.cos(angle),
    ];
  }
  const offset: Position = [
    current[0] - CAMERA_TARGET[0],
    current[1] - CAMERA_TARGET[1],
    current[2] - CAMERA_TARGET[2],
  ];
  const distance = Math.hypot(...offset);
  if (distance === 0) return [...DEFAULT_CAMERA_POSITION];
  const factor = action === "zoom-in" ? 0.82 : 1.22;
  const boundedDistance = Math.min(
    MAX_CAMERA_DISTANCE,
    Math.max(MIN_CAMERA_DISTANCE, distance * factor),
  );
  const scale = boundedDistance / distance;
  return CAMERA_TARGET.map(
    (coordinate, index) => coordinate + offset[index] * scale,
  ) as Position;
}

function CameraControls({ command }: { command: ViewCommand }) {
  const camera = useThree((state) => state.camera);
  const invalidate = useThree((state) => state.invalidate);
  useEffect(() => {
    const next = nextCameraPosition(command.action, [
      camera.position.x,
      camera.position.y,
      camera.position.z,
    ]);
    camera.position.set(...next);
    camera.lookAt(...CAMERA_TARGET);
    invalidate();
  }, [camera, invalidate, command]);
  return (
    <OrbitControls
      makeDefault
      target={CAMERA_TARGET}
      enablePan={false}
      minDistance={MIN_CAMERA_DISTANCE}
      maxDistance={MAX_CAMERA_DISTANCE}
      maxPolarAngle={Math.PI / 2.05}
      enableDamping={false}
    />
  );
}

function BenchScene({
  state,
  command,
}: {
  state: SceneState;
  command: ViewCommand;
}) {
  return (
    <>
      <ambientLight intensity={1.15} />
      <directionalLight
        position={[4, 8, 6]}
        intensity={2.2}
        castShadow
        shadow-mapSize={[1024, 1024]}
      />
      <mesh position={[0, -0.12, 0]} receiveShadow>
        <boxGeometry args={[10, 0.2, 4.5]} />
        <meshStandardMaterial color="#d7e0db" roughness={0.8} />
      </mesh>
      <Cabinet state={state} />
      <LoadedItems items={state.items} />
      {state.culture.spentMedium && (
        <Label position={[-1.4, 2.85, -1.6]}>
          Spent medium removed · {state.culture.spentMedium}
        </Label>
      )}
      {state.culture.freshMedium && (
        <Label position={[1.4, 2.85, -1.6]}>
          Fresh medium added · {state.culture.freshMedium}
        </Label>
      )}
      <ContactShadows
        key={state.description}
        frames={1}
        position={[0, 0.01, 0]}
        opacity={0.25}
        scale={12}
        blur={2.5}
        far={5}
      />
      <CameraControls command={command} />
    </>
  );
}

class GraphicsBoundary extends Component<
  { children: ReactNode; onFailure: () => void },
  { failed: boolean }
> {
  state = { failed: false };
  static getDerivedStateFromError() {
    return { failed: true };
  }
  componentDidCatch() {
    this.props.onFailure();
  }
  render() {
    return this.state.failed ? null : this.props.children;
  }
}

export default function AsepticBench3D({ panels }: { panels: Panels }) {
  const [failed, setFailed] = useState(false);
  const [command, setCommand] = useState<ViewCommand>({
    action: "reset",
    revision: 0,
  });
  const state = asepticSceneState(panels);
  const updateView = (action: ViewCommand["action"]) =>
    setCommand((current) => ({ action, revision: current.revision + 1 }));
  return (
    <section className="card bench-3d" aria-labelledby="aseptic-3d-title">
      <div className="bench-3d-heading">
        <div>
          <h3 id="aseptic-3d-title">Interactive 3D cabinet</h3>
          <p>
            Drag to orbit, or use the rotate buttons. Scroll, pinch or use the
            buttons to zoom. Use the action form to perform and assess every
            step.
          </p>
        </div>
        <span className="bench-3d-badge">Visual model · not to scale</span>
      </div>
      {!failed && (
        <div role="group" aria-label="3D view controls">
          <button type="button" onClick={() => updateView("rotate-left")}>
            Rotate left
          </button>{" "}
          <button type="button" onClick={() => updateView("rotate-right")}>
            Rotate right
          </button>{" "}
          <button type="button" onClick={() => updateView("zoom-in")}>
            Zoom in
          </button>{" "}
          <button type="button" onClick={() => updateView("zoom-out")}>
            Zoom out
          </button>{" "}
          <button type="button" onClick={() => updateView("reset")}>
            Reset 3D view
          </button>
        </div>
      )}
      {failed ? (
        <p role="status">
          3D graphics are unavailable in this browser. Use the text description,
          bench-state tables and action form below.
        </p>
      ) : (
        <GraphicsBoundary onFailure={() => setFailed(true)}>
          <div className="bench-3d-canvas">
            <Canvas
              role="region"
              aria-label="Procedural Class II cabinet illustration"
              aria-describedby="aseptic-3d-description"
              frameloop="demand"
              camera={{ position: DEFAULT_CAMERA_POSITION, fov: 43 }}
              dpr={[1, 1.5]}
              fallback={
                <p>
                  WebGL is unavailable. Use the text description, bench-state
                  tables and action form below.
                </p>
              }
              onCreated={({ gl }) => {
                gl.domElement.addEventListener(
                  "webglcontextlost",
                  () => setFailed(true),
                  { once: true },
                );
              }}
            >
              <Suspense fallback={null}>
                <BenchScene state={state} command={command} />
              </Suspense>
            </Canvas>
          </div>
        </GraphicsBoundary>
      )}
      <details>
        <summary>Text description and visible readings</summary>
        <p id="aseptic-3d-description">{state.description}</p>
      </details>
      <p className="muted">
        This illustrative scene reports only visible panel state. It does not
        reveal undisclosed conditions, model airflow or contamination, measure
        hand movements, or provide physical aseptic-technique training.
        Pathologically crowded or unrecognized layouts may require approximate
        overlapping slots; the visible text readings remain authoritative.
      </p>
    </section>
  );
}
