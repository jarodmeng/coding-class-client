-- FinishLine.server.lua
-- When a player touches the FinishLine, check if they have enough Coins. If yes, tell them they win.

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local finishPart = script.Parent
local REQUIRED_COINS = 10

-- Ensure WinEvent exists (shared message channel server -> client)
local winEvent = ReplicatedStorage:FindFirstChild("WinEvent")
if not winEvent then
    winEvent = Instance.new("RemoteEvent")
    winEvent.Name = "WinEvent"
    winEvent.Parent = ReplicatedStorage
end

local recent = {} -- [Player] = true

local function getPlayerFromHit(hit: BasePart): Player?
    local character = hit.Parent
    if not character then return nil end
    return Players:GetPlayerFromCharacter(character)
end

local function getCoins(player: Player): number?
    local leaderstats = player:FindFirstChild("leaderstats")
    if not leaderstats then return nil end
    local coins = leaderstats:FindFirstChild("Coins")
    if not coins then return nil end
    return coins.Value
end

finishPart.Touched:Connect(function(hit)
    local player = getPlayerFromHit(hit)
    if not player then return end

    if recent[player] then return end
    recent[player] = true

    local coins = getCoins(player)
    if coins == nil then
        winEvent:FireClient(player, "No Coins found yet!")
    elseif coins >= REQUIRED_COINS then
        winEvent:FireClient(player, "YOU WIN! (" .. tostring(coins) .. "/" .. tostring(REQUIRED_COINS) .. ")")
        -- Optional: reset checkpoint so next round starts at the beginning
        player.RespawnLocation = nil
    else
        winEvent:FireClient(player, "Need " .. tostring(REQUIRED_COINS) .. " coins! (" .. tostring(coins) .. "/" .. tostring(REQUIRED_COINS) .. ")")
    end

    task.delay(1, function()
        recent[player] = nil
    end)
end)
