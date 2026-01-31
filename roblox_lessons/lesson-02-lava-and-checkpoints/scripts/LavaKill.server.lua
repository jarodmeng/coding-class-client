-- LavaKill.server.lua
-- Touching this part kills the player (server-side)

local lavaPart = script.Parent
local recent = {} -- [Humanoid] = true (simple debounce)

lavaPart.Touched:Connect(function(hit)
    local character = hit.Parent
    if not character then return end

    local humanoid = character:FindFirstChildOfClass("Humanoid")
    if not humanoid then return end

    if recent[humanoid] then return end
    recent[humanoid] = true

    humanoid.Health = 0

    task.delay(1, function()
        recent[humanoid] = nil
    end)
end)
