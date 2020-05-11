from Section12_Proxy.VirtualProxy.LazyBitmap import LazyBitmap


def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')


if __name__ == '__main__':
    bmp = LazyBitmap('facepalm.jpg')  # Bitmap
    draw_image(bmp)
