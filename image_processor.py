from PIL import Image, ImageFilter
import sys
import os

# Function for converting the image format
def img_convert(img, out_file):
    try:
        if not img.format == 'PNG':
            img.save(out_file, 'PNG')
            print(f"Image converted and saved as {out_file} in PNG format")
        elif not img.format == 'JPEG':
            img.save(out_file, 'JPEG')
            print(f"Image converted and saved as {out_file} in JPEG format")
        return out_file
    except Exception as e:
        print(f"An error occurred: {e}")

# Function for applying a blur effect to the image
def img_blur(img, out_file):
    try:
        blurred_img = img.filter(ImageFilter.BLUR)
        blurred_img.save(out_file)
        print(f"Image blurred and saved as {out_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function for applying a sharpening effect to the image
def img_sharpen(img, out_file):
    try:
        sharpened_img = img.filter(ImageFilter.SHARPEN)
        sharpened_img.save(out_file)
        print(f"Image sharpened and saved as {out_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function for rotating the image
def img_rotate(img, out_file):
    try:
        angle = input('angle: ')  # Prompt the user for the rotation angle
        rotated_img = img.rotate(angle)
        rotated_img.save(out_file)
        print(f"Image rotated by {angle} degrees and saved as {out_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function for resizing the image
def img_resize(img, out_file):
    try:
        width = input('width: ')  # Prompt the user for the desired width
        height = input('height: ')  # Prompt the user for the desired height
        resized_img = img.resize((width, height))
        resized_img.save(out_file)
        print(f"Image resized and saved as {out_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function for creating a thumbnail of the image
def img_thumbnail(img, out_file, size):
    try:
        thumbnail_img = img.copy()
        thumbnail_img.thumbnail(size)
        thumbnail_img.save(out_file)
        print(f"Thumbnail image created and saved as {out_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to generate the output path for the processed image
def get_output_path(name, action):
    out_folder = './output_folder'
    out_name = f'{name}_{action}'
    output_path = os.path.join(out_folder, out_name)
    
    #if the file aready exists then we will create a new file with a counter
    count = 1
    while os.path.exists(output_path):
        output_path = f'{output_path}_{count}'
        count += 1  #the counter shifts to the next number as soon as we name the file
    return output_path

if __name__ == '__main__':
    #Handle command line arguments: Use the sys module to access command line arguments. You can use sys.argv to retrieve the command line arguments passed to your script.
    args = sys.argv[1:]  # Exclude the script name from the arguments

    # Check if any command line arguments are provided
    if len(args) == 0:
        print("No command line arguments provided. Please provide the necessary arguments.")
        sys.exit(1)

    valid_image_paths = []

    # Set the folder path where the images are located
    in_folder = './input_folder'

    #check if image exists in library and if it does not remove it from the list and tell the user that the images we will perform the action on are these and failed to open the other images 
    for arg in args:
        image_path = os.path.join(in_folder, arg)
        if os.path.isfile(image_path):
            valid_image_paths.append(image_path)
        else:
            print(f'{arg} does not exist')

    # Provide feedback to the user about the valid images
    print("The following images will be processed:")
    for path in valid_image_paths:
        _, image_name = os.path.split(path)
        print(image_name)

    # Remove invalid images from the list
    args = valid_image_paths

    #Process the images: Use the functions you defined earlier to process the images based on the command line arguments provided.
    for arg in args:
        img = Image.open(arg)
        # Ask the user what action they want to perform on the image
        action = input(f"What action do you want to perform on the image {arg}? (1.convert 2.blur 3.sharpen 4.rotate 5.resize 6.thumbnail) \n")
        
        # Get the output image path based on the action performed
        output_image_path = get_output_path(os.path.basename(arg), action)

        #Perform the chosen action on the image and save the processed image to the output folder
        if action == 'convert':
            img_convert(img, output_image_path)
        elif action == 'blur':
            img_blur(img, output_image_path)
        elif action == 'sharpen':
            img_sharpen(img, output_image_path)
        elif action == 'rotate':
            img_rotate(img, output_image_path)
        elif action == 'resize':
            img_resize(img, output_image_path)
        elif action == 'thumbnail':
            img_thumbnail(img, output_image_path)
        else:
            print('No action performed on the image')