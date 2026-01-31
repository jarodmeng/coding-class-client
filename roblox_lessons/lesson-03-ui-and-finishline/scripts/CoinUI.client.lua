-- CoinUI.client.lua
-- Shows Coins on the player's screen and displays a win message when the server says "You Win!"

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local player = Players.LocalPlayer
local playerGui = player:WaitForChild("PlayerGui")

-- Create ScreenGui
local screenGui = Instance.new("ScreenGui")
screenGui.Name = "HUD"
screenGui.ResetOnSpawn = false
screenGui.Parent = playerGui

-- Coins label
local coinsLabel = Instance.new("TextLabel")
coinsLabel.Name = "CoinsLabel"
coinsLabel.Size = UDim2.new(0, 240, 0, 50)
coinsLabel.Position = UDim2.new(0, 20, 0, 20)
coinsLabel.BackgroundTransparency = 0.3
coinsLabel.TextScaled = true
coinsLabel.Text = "Coins: 0"
coinsLabel.Parent = screenGui

-- Win label (hidden by default)
local winLabel = Instance.new("TextLabel")
winLabel.Name = "WinLabel"
winLabel.Size = UDim2.new(0, 500, 0, 120)
winLabel.Position = UDim2.new(0.5, -250, 0.4, 0)
winLabel.BackgroundTransparency = 0.2
winLabel.TextScaled = true
winLabel.Text = "YOU WIN!"
winLabel.Visible = false
winLabel.Parent = screenGui

-- Update coins whenever leaderstats changes
local function hookLeaderstats()
    local leaderstats = player:WaitForChild("leaderstats")
    local coins = leaderstats:WaitForChild("Coins")

    local function update()
        coinsLabel.Text = "Coins: " .. tostring(coins.Value)
    end

    update()
    coins.Changed:Connect(update)
end

task.spawn(hookLeaderstats)

-- Listen for win event from server
local winEvent = ReplicatedStorage:WaitForChild("WinEvent")
winEvent.OnClientEvent:Connect(function(message)
    winLabel.Text = message or "YOU WIN!"
    winLabel.Visible = true
    task.delay(3, function()
        winLabel.Visible = false
    end)
end)
