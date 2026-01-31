# Roblox + Cursor Lesson 1: Coin Collector (Free Tier Friendly)

This folder contains everything you need for **Lesson 1**:
- Cursor Project Rules (kid-friendly)
- Two Roblox scripts (Leaderstats + Coin)
- A tiny prompt cheatsheet

## 1) Install Cursor Rules (recommended)
These rules make Cursor behave like a Roblox teacher and keep answers short.

**Do this in the roblox_lessons folder (the one that contains this lesson):**
- Keep the folder: `.cursor/rules/`

Cursor will auto-apply rules when you open the project in Cursor.

## 2) Lesson 1 Goal
Touch a coin → coin disappears → your Coins score goes up by 1.

## 3) Roblox Studio Setup (step-by-step)

### Step A: Create leaderstats (Coins)
1. Open **Roblox Studio**
2. Go to **ServerScriptService**
3. Add a **Script** named `Leaderstats`
4. Copy and paste:
   - `scripts/Leaderstats.server.lua`

✅ Test:
- Press **Play**
- You should see a leaderboard appear showing **Coins = 0**

### Step B: Create a Coin part
1. In **Workspace**, insert a **Part**
2. Rename it to: `Coin`
3. Set:
   - Anchored = true
   - (Optional) Shape = Ball

### Step C: Add Coin script
1. Under `Coin`, insert a **Script**
2. Name it: `CoinScript`
3. Copy and paste:
   - `scripts/CoinScript.server.lua`

✅ Test:
- Press **Play**
- Touch the coin
- Coins should become **1** and the coin should disappear

## 4) Optional Upgrade: Coin respawns after 5 seconds
Replace `coinPart:Destroy()` with the snippet:
- `scripts/CoinRespawnSnippet.lua`

## 5) If something breaks
Copy the script + the red Output error into Cursor and ask:

> Fix it with the smallest change. Explain like I'm 10. Then give me one tiny upgrade.

Good luck and have fun!
