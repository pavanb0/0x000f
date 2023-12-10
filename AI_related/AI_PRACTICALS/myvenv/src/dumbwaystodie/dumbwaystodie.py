from stegano import lsb

image_path = 'D:\\pavanReact\\0x000f\\AI_related\\AI_PRACTICALS\\myvenv\\src\\dumbwaystodie\\RomanianMap.png'
data_to_hide = """
dict_hn={'Arad':336,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
         'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
         'Mehadia':241,'Neamt':234,'Oradea':380,'Pitesti':100,'Rimnicu':193,
         'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}

dict_gn={
        'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
        'Bucharest': {'Urziceni': 85, 'Giurgiu': 90, 'Pitesti': 101, 'Fagaras': 211},
        'Craiova': {'Drobeta': 120, 'Pitesti': 138, 'Rimnicu': 146},
        'Drobeta': {'Mehadia': 75, 'Craiova': 120},
        'Eforie': {'Hirsova': 86},
        'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
        'Giurgiu': {'Bucharest': 90},
        'Hirsova': {'Eforie': 86, 'Urziceni': 98},
        'Iasi': {'Neamt': 87, 'Vaslui': 92},
        'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
        'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
        'Neamt': {'Iasi': 87},
        'Oradea': {'Zerind': 71, 'Sibiu': 151},
        'Pitesti': {'Rimnicu': 97, 'Bucharest': 101, 'Craiova': 138},
        'Rimnicu': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
        'Sibiu': {'Rimnicu': 80, 'Fagaras': 99, 'Arad': 140, 'Oradea': 151},
        'Timisoara': {'Lugoj': 111, 'Arad': 118},
        'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
        'Vaslui': {'Iasi': 92, 'Urziceni': 142},
        'Zerind': {'Oradea': 71, 'Arad': 75}
    }
"""

output_image = "D:\\pavanReact\\0x000f\\AI_related\\AI_PRACTICALS\\myvenv\\src\\dumbwaystodie\\output_image.png"
secret_image = lsb.reveal(output_image)
print(secret_image)

# secret_image.save('output_image.png')