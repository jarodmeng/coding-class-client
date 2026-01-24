-- Upgrade: CoinRespawnSnippet.lua
-- Replace `coinPart:Destroy()` with this block if you want the coin to respawn after 5 seconds.

coinPart.Transparency = 1
coinPart.CanCollide = false
task.wait(5)
coinPart.Transparency = 0
coinPart.CanCollide = true
touched = false
