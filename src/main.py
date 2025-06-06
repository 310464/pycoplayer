from screen import ImageType
import screen
import cv2
import torchvision.models

Region = {
    "top": 300,
    "left": 1150,
    "width": 1500,
    "height": 500
}

screens = screen.AIScreenshot()
screens.take_screenshot(region=True, region_area=Region)
screens.show_screenshot(ImageType.GrayscaleImage)


# tensor = screens.transform_to_tensor(ImageType.GrayscaleImage)
# pool = torch.nn.MaxPool2d(2, 2)
# downsample_tensor = pool(tensor) # image output (120, 120)
# input_batch = downsample_tensor.unsqueeze(0)
# input_batch = input_batch.to('device')
# model = coolai.NeuralNetwork(input_batch, )

# resnet_model = torchvision.models.resnet18(pretrained=True)
# resnet_model = torch.nn.Sequential(*list(resnet_model.children()))[:-1]
# resnet_model.eval()


# cv2.destroyAllWindows()