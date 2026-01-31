# Roblox + Cursor Lesson 3: UI + Finish Line (Free Tier Friendly)

Lesson 3 adds:
1) A **Coins UI** on the screen (client-side)
2) A **FinishLine** that checks if you have enough Coins (server-side) and shows a message

This lesson assumes you already have **Coins leaderstats** from Lesson 1.

---

## Part A: Coins UI (client-side)

### 1) Where to put the UI script
In **StarterGui**:
1. Insert a **ScreenGui** (name it `HUD` if you want)
2. Inside that ScreenGui, insert a **LocalScript** named `CoinUI`

Paste the code from:
- `lessons/lesson-03-ui-and-finishline/scripts/CoinUI.client.lua`

✅ Test:
- Press **Play**
- You should see `Coins: 0` at the top-left
- Touch a coin → number should change

**Common mistake:** If you put a LocalScript in Workspace, it will not run.

---

## Part B: Finish line win condition (server-side)

### 1) Create the finish line part
In **Workspace**:
1. Insert a **Part**
2. Rename it to: `FinishLine`
3. Set:
   - Anchored = true
   - (Optional) Color = green
   - Place it at the end of your obby

### 2) Add the FinishLine Script
1. Under `FinishLine`, insert a **Script** named `FinishLine`
2. Paste the code from:
- `lessons/lesson-03-ui-and-finishline/scripts/FinishLine.server.lua`

This script:
- checks if you have **REQUIRED_COINS** (default 10)
- sends a message to your UI using a RemoteEvent named **WinEvent**
- auto-creates WinEvent in **ReplicatedStorage** if missing

✅ Test:
- Press **Play**
- Touch FinishLine with < 10 coins → message says you need more
- Touch FinishLine with >= 10 coins → message says YOU WIN

---

## Tiny upgrades (pick one)
- Change REQUIRED_COINS to 5 or 20
- Add a sound when you win
- Teleport the player back to the start when they win

Use `CURSOR_PROMPTS.md` for efficient prompts.
