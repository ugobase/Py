# name = ["Ugochukwu", "Chike", "Ikenna"]
# surname = ["Mgboji"]
# for x in name:
#     for y in surname:
#         print(x, y)

# name = ["Ugochukwu", "Chike", "Ikenna"]
# trait = ["is_kind", "is_handsome", "is_rich"]
# for x in name:
#     for y in trait:
#         print(x, y)

name = ["Ugochukwu", "Chike", "Ikenna"]
for x in name:
    print(x)             # Breaks after Chike
    if x == "Chike":
        break
    #print(x)
print("End!")


name = ["Ugochukwu", "Chike", "Ikenna"]
for x in name:
    #print(x)
    if x == "Ikenna":
        break
    print(x)           # Breaks after Chike
print("End!")


name = ["Ugochukwu", "Chike", "Ikenna"]
for x in name:
    if x == "Chike":
        continue
    print(x)           # Skips Chike
print("End!")


name = ["Ugochukwu", "Chike", "Ikenna"]
for x in name:
    print(x)             # Skips no one
    if x == "Chike":
        continue
    #print(x)
print("End!")