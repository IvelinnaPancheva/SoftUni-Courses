materials = dict()
key_materials = ["shards", "fragments", "motes"]
legendary_item_not_obtained = True

while legendary_item_not_obtained:
    data = input().split(" ")

    for index in range(0, len(data),2):
        current_quantity = int(data[index])
        current_material = data[index +1].lower()

        if current_material not in materials:
            materials[current_material] = current_quantity
        else:
            materials[current_material] += current_quantity

        if current_material in key_materials and materials[current_material] >= 250:

            legendary_item_not_obtained = False
            materials[current_material] -= 250
            if current_material == "shards":
                legendary_item = "Shadowmourne"
            elif current_material == "fragments":
                legendary_item = "Valanyr"
            elif current_material == "motes":
                legendary_item = "Dragonwrath"
            print(f"{legendary_item} obtained!")

            for material in key_materials:
                if material in materials:
                    print(f"{material}: {materials[material]}")
                else:
                    print(f"{material}: {0}")
            for material in materials:
                if material not in key_materials:
                    print(f"{material}: {materials[material]}")

            break




