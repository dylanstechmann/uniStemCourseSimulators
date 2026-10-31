import { Component, Suspense, useState, type ReactNode } from "react";
import { Canvas } from "@react-three/fiber";
import { ContactShadows, Html, OrbitControls } from "@react-three/drei";
import type { BenchRun } from "../types";

export function pipetteSceneState(run: BenchRun) {
  const rows = run.panels.flatMap((panel) => panel.rows);
  const value = (label: string) =>
    rows.find(([name]) => name === label)?.[1] ?? "";
  const volume = value("Volume setting");
  const tip = value("Tip");
  const liquid = value("In tip");
  const balance = value("Balance");
  return {
    volume,
    hasTip: tip.startsWith("fitted"),
    prewetted: tip.includes("pre-wetted"),
    hasLiquid: liquid.startsWith("water"),
    balance: balance.split(" displayed")[0] || "0.0 mg",
    temperature: value("Water temperature"),
    readings: value("Readings recorded") || "0",
    description: `Three-dimensional bench. Pipette set to ${volume}. Tip: ${tip}. In tip: ${liquid}. ${balance}. Water temperature: ${value("Water temperature")}.`,
  };
}

type SceneState = ReturnType<typeof pipetteSceneState>;

function Label({
  children,
  position,
}: {
  children: ReactNode;
  position: [number, number, number];
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

function Pipette({ state }: { state: SceneState }) {
  return (
    <group position={[-1.6, 1.55, 0.25]} rotation={[0, 0, -0.12]}>
      <mesh position={[0, 0.95, 0]} castShadow>
        <cylinderGeometry args={[0.13, 0.13, 0.22, 32]} />
        <meshStandardMaterial color="#d8513f" roughness={0.35} />
      </mesh>
      <mesh position={[0, 0.76, 0]} castShadow>
        <cylinderGeometry args={[0.075, 0.075, 0.25, 24]} />
        <meshStandardMaterial
          color="#c4cdd0"
          metalness={0.65}
          roughness={0.25}
        />
      </mesh>
      <mesh position={[0, 0.12, 0]} castShadow>
        <cylinderGeometry args={[0.24, 0.24, 1.1, 40]} />
        <meshStandardMaterial color="#edf1ee" roughness={0.3} />
      </mesh>
      <mesh position={[0, 0.42, 0]} castShadow>
        <cylinderGeometry args={[0.245, 0.245, 0.28, 40]} />
        <meshStandardMaterial color="#286b56" roughness={0.35} />
      </mesh>
      <mesh position={[0, 0.18, 0.242]}>
        <boxGeometry args={[0.25, 0.24, 0.015]} />
        <meshStandardMaterial color="#152b25" />
      </mesh>
      <Html
        position={[0, 0.18, 0.26]}
        center
        className="pipette-display"
        distanceFactor={10}
      >
        {state.volume.replace(" µL", "")}
      </Html>
      <mesh position={[0, -0.56, 0]} castShadow>
        <cylinderGeometry args={[0.18, 0.1, 0.3, 32]} />
        <meshStandardMaterial color="#d5dcd9" roughness={0.3} />
      </mesh>
      {state.hasTip && (
        <group>
          <mesh position={[0, -0.99, 0]} castShadow>
            <cylinderGeometry args={[0.095, 0.018, 0.62, 32]} />
            <meshStandardMaterial
              color="#d9edf0"
              transparent
              opacity={0.75}
              roughness={0.15}
            />
          </mesh>
          {state.hasLiquid && (
            <mesh position={[0, -1.05, 0]}>
              <cylinderGeometry args={[0.065, 0.018, 0.38, 24]} />
              <meshStandardMaterial
                color="#4aaac2"
                transparent
                opacity={0.85}
              />
            </mesh>
          )}
        </group>
      )}
      <Label position={[0, 1.35, 0]}>Micropipette · {state.volume}</Label>
      {state.hasLiquid && <Label position={[0, -1.45, 0]}>Water in tip</Label>}
    </group>
  );
}

function Balance({ state }: { state: SceneState }) {
  return (
    <group position={[1.45, 0.15, 0.15]}>
      <mesh castShadow receiveShadow>
        <boxGeometry args={[2.25, 0.3, 1.8]} />
        <meshStandardMaterial color="#e5e9e7" roughness={0.35} />
      </mesh>
      <mesh position={[0, 0.18, 0.15]} castShadow>
        <cylinderGeometry args={[0.7, 0.7, 0.09, 48]} />
        <meshStandardMaterial
          color="#aebdc2"
          metalness={0.75}
          roughness={0.25}
        />
      </mesh>
      <mesh position={[0, 0.43, 0.15]} castShadow>
        <cylinderGeometry args={[0.43, 0.32, 0.45, 40, 1, true]} />
        <meshStandardMaterial
          color="#e6f2f2"
          transparent
          opacity={0.55}
          side={2}
        />
      </mesh>
      <mesh position={[0, 0.22, 0.15]}>
        <cylinderGeometry args={[0.32, 0.32, 0.025, 40]} />
        <meshStandardMaterial color="#63b5c9" transparent opacity={0.8} />
      </mesh>
      <mesh position={[0, 0.02, 0.91]}>
        <boxGeometry args={[1.05, 0.18, 0.025]} />
        <meshStandardMaterial color="#142b25" />
      </mesh>
      <Html
        position={[0, 0.03, 0.94]}
        center
        className="balance-display"
        distanceFactor={10}
      >
        {state.balance}
      </Html>
      <Label position={[0, 0.95, 0]}>Analytical balance</Label>
    </group>
  );
}

function Reservoir({ state }: { state: SceneState }) {
  return (
    <group position={[-1.6, 0.18, 0.25]}>
      <mesh castShadow>
        <cylinderGeometry args={[0.65, 0.55, 0.3, 40, 1, true]} />
        <meshStandardMaterial
          color="#d8e5e4"
          transparent
          opacity={0.7}
          side={2}
        />
      </mesh>
      <mesh position={[0, -0.08, 0]}>
        <cylinderGeometry args={[0.54, 0.54, 0.08, 40]} />
        <meshStandardMaterial color="#54b1c8" transparent opacity={0.85} />
      </mesh>
      <Label position={[0, -0.5, 0]}>Water · {state.temperature}</Label>
    </group>
  );
}

function TipRack() {
  return (
    <group position={[-3.25, 0.22, -0.65]}>
      <mesh castShadow>
        <boxGeometry args={[1.05, 0.38, 1.35]} />
        <meshStandardMaterial color="#397d68" roughness={0.4} />
      </mesh>
      {[-0.3, 0, 0.3].flatMap((x) =>
        [-0.42, 0, 0.42].map((z) => (
          <mesh key={`${x}:${z}`} position={[x, 0.32, z]} castShadow>
            <cylinderGeometry args={[0.075, 0.014, 0.48, 16]} />
            <meshStandardMaterial color="#d9edf0" transparent opacity={0.8} />
          </mesh>
        )),
      )}
      <Label position={[0, 0.85, 0]}>New tips</Label>
    </group>
  );
}

function BenchScene({ state }: { state: SceneState }) {
  return (
    <>
      <ambientLight intensity={1.1} />
      <directionalLight
        position={[3, 7, 5]}
        intensity={2.4}
        castShadow
        shadow-mapSize={[1024, 1024]}
      />
      <mesh position={[0, -0.12, 0]} receiveShadow>
        <boxGeometry args={[9, 0.2, 5]} />
        <meshStandardMaterial color="#d9e3dc" roughness={0.75} />
      </mesh>
      <Pipette state={state} />
      <Balance state={state} />
      <Reservoir state={state} />
      <TipRack />
      <ContactShadows
        position={[0, 0.01, 0]}
        opacity={0.3}
        scale={12}
        blur={2.5}
        far={5}
      />
      <OrbitControls
        makeDefault
        target={[0, 0.65, 0]}
        minDistance={5}
        maxDistance={14}
        maxPolarAngle={Math.PI / 2.05}
        enableDamping={false}
      />
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

export default function PipetteBench3D({ run }: { run: BenchRun }) {
  const [failed, setFailed] = useState(false);
  const state = pipetteSceneState(run);
  return (
    <section className="card bench-3d" aria-labelledby="bench-3d-title">
      <div className="bench-3d-heading">
        <div>
          <h3 id="bench-3d-title">Interactive 3D bench</h3>
          <p>
            Drag to orbit. Scroll or pinch to zoom. Use the action form to
            perform each step.
          </p>
        </div>
        <span className="bench-3d-badge">Visual model · not to scale</span>
      </div>
      {failed ? (
        <p role="status">
          3D graphics are unavailable in this browser. All readings and actions
          remain available below.
        </p>
      ) : (
        <GraphicsBoundary onFailure={() => setFailed(true)}>
          <div className="bench-3d-canvas">
            <Canvas
              aria-label={state.description}
              camera={{ position: [6.5, 5.2, 8.5], fov: 42 }}
              dpr={[1, 1.5]}
              fallback={
                <p>
                  WebGL is unavailable. Use the bench-state tables and action
                  form below.
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
                <BenchScene state={state} />
              </Suspense>
            </Canvas>
          </div>
        </GraphicsBoundary>
      )}
      <p className="sr-only">{state.description}</p>
      <p className="muted">
        The illustration shows server-reported state. It does not measure
        technique, immersion depth, or physical competency.
      </p>
    </section>
  );
}
