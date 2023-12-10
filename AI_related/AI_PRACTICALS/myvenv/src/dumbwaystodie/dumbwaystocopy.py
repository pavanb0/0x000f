from stegano import lsb
output_image_path = 'D:\\pavanReact\\0x000f\\AI_related\\AI_PRACTICALS\\myvenv\\src\\dumbwaystodie\\output_image.png'
hidden_data = lsb.reveal(output_image_path)
print(hidden_data)
