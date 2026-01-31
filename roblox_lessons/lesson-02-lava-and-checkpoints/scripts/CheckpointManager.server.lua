-- CheckpointManager.server.lua
-- Lets SpawnLocations act like checkpoints (server-side)
-- Put this Script in ServerScriptService.

local Players = game:GetService("Players")

local CHECKPOINTS_FOLDER_NAME = "Checkpoints"

local checkpointsFolder = workspace:FindFirstChild(CHECKPOINTS_FOLDER_NAME)
if not checkpointsFolder then
    warn(("CheckpointManager: Create a Folder in Workspace named '%s' and put SpawnLocations inside it."):format(CHECKPOINTS_FOLDER_NAME))
    return
end

local function isCharacterHit(hit: Instance): boolean
    return hit and hit.Parent and hit.Parent:FindFirstChildOfClass("Humanoid") ~= nil
end

local function getPlayerFromHit(hit: Instance): Player?
    if not isCharacterHit(hit) then return nil end
    return Players:GetPlayerFromCharacter(hit.Parent)
end

local function activateCheckpoint(spawn: SpawnLocation, player: Player)
    player.RespawnLocation = spawn
    spawn.BrickColor = BrickColor.new("Lime green")
end

for _, obj in ipairs(checkpointsFolder:GetChildren()) do
    if obj:IsA("SpawnLocation") then
        local spawn = obj
        spawn.Neutral = true
        spawn.Enabled = true

        spawn.Touched:Connect(function(hit)
            local player = getPlayerFromHit(hit)
            if not player then return end
            activateCheckpoint(spawn, player)
        end)
    end
end
