-- CoinScript.server.lua
-- When a player touches this coin, they gain 1 coin and the coin disappears

local Players = game:GetService("Players")

local coinPart = script.Parent
local touched = false

coinPart.Touched:Connect(function(hit)
    if touched then return end

    local character = hit.Parent
    local player = Players:GetPlayerFromCharacter(character)
    if not player then return end

    touched = true

    local leaderstats = player:FindFirstChild("leaderstats")
    if not leaderstats then return end

    local coins = leaderstats:FindFirstChild("Coins")
    if not coins then return end

    coins.Value += 1
    coinPart:Destroy()
end)
