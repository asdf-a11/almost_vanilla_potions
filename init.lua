--TODO i dont think honey's texture has been overloaded but that is something for the future
--TODO i want to include some more example images in game of the textures

--Some potions dont seem to be supported by this texture pack
local overrideList = {
	"awkward",
	"mundane",
	"thick",
	"healing",
	"harming",
	"night_vision",
	--"swiftness",
	"slowness",
	--"leaping",
	--"withering",
	"poison",
	"regeneration",
	"invisibility",
	"water_breathing",
	"fire_resistance",
	"strength",
	"weakness",
	"slow_falling",
	"turtle_master",
	"luck",
	"bad_luck",
	--"ominous",
	--"infestation",
	"oozing",
	"weaving",
	"wind_charged"
}

for i = 1, #overrideList do
    local catList = {"", "_splash", "_lingering"}
    for j = 1, #catList do
        local cat = catList[j]
        local potionName = overrideList[i] .. cat
        
        
        local imageName = "mcl_potions_"..potionName..".png"
        local potionRegistryName = "mcl_potions:" .. potionName
        if core.registered_items[potionRegistryName] then
            core.override_item(potionRegistryName, {
                inventory_image = imageName,
                tiles = {imageName},
                wield_image = imageName,
                wield_mesh = nil
            })
        else
            --Just left this in because
        end
    end
end


--Sometimes use this for debugging
--minetest.register_globalstep(function()
--    local player = core.get_player_by_name("singleplayer")
--    if not player then return end
--    local item = player:get_wielded_item()
--    core.chat_send_all("Holding: " .. item:get_name())
--end)