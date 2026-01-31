# Roblox + Cursor Lesson 2: Lava + Checkpoints (Free Tier Friendly)

Lesson 2 adds two classic obby features:
1) **Lava** that kills you on touch
2) **Checkpoints** so you respawn further into the level

---

## Part A: Lava that kills you

### 1) Create the lava part
In **Workspace**:
1. Insert a **Part**
2. Rename it to: `Lava`
3. Set:
   - Anchored = true
   - (Optional) Material = Neon
   - (Optional) Color = bright red/orange
4. Make it a big flat rectangle under some obstacle.

### 2) Add the lava Script
1. Under `Lava`, insert a **Script** named `LavaKill`
2. Paste the code from:
   - `lessons/lesson-02-lava-and-checkpoints/scripts/LavaKill.server.lua`

✅ Test:
- Press **Play**
- Touch `Lava`
- Your character should die and respawn

---

## Part B: Checkpoints (respawn where you last touched)

### 1) Create a checkpoints folder
In **Workspace**:
1. Insert a **Folder**
2. Name it exactly: `Checkpoints`

### 2) Add checkpoint spawn pads
Inside `Workspace/Checkpoints`:
1. Insert **SpawnLocation** (not just a Part)
2. Rename it: `CP1`
3. Copy it a few times:
   - `CP2`, `CP3`, etc.
4. Place them along the course.

### 3) Add the checkpoint manager Script
In **ServerScriptService**:
1. Insert a **Script** named `CheckpointManager`
2. Paste the code from:
   - `lessons/lesson-02-lava-and-checkpoints/scripts/CheckpointManager.server.lua`

✅ Test:
1. Press **Play**
2. Walk onto `CP2`
3. Touch the lava (die)
4. You should respawn at `CP2`

---

## Common mistakes
- You used a **LocalScript** (won't work). Use **Script** for this lesson.
- Your folder name is not exactly `Checkpoints`.
- You used a **Part** instead of a **SpawnLocation**.

Use `CURSOR_PROMPTS.md` for efficient prompts.
