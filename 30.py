from PIL import Image


def create_image_and_string(file_name):
  with open('yankeedoodle.csv') as f:
    image_data = [d.strip() for d in f.read().split(',')]

    # img dimensions are factors of data length
    image = Image.new('F', (53, 139))
    image.putdata([float(d) for d in image_data], scale=200)
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    image = image.transpose(Image.ROTATE_90)

    # resulting gif says which indexes to search for
    string_data = [
      chr(int(image_data[i][5] + image_data[i + 1][5] + image_data[i + 2][6]))
      for i in range(0,
                     len(image_data) - 2, 3)
    ]
    return ''.join(string_data)


if __name__ == '__main__':
  file_name = 'yankeedoodle.csv'
  image_string = create_image_and_string(file_name)
  print(image_string)
