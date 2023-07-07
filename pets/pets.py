
import torch
from torchvision.models import ResNet18_Weights
#model = resnet18
model=torch.load('pets/pets_model.pth',map_location='mps')
weights = torch.load('pets/pets_weights.pth',map_location='mps')
model.load_state_dict(weights)
pet_map={0:'Кот',1:'Пес'}
def get_pet(img):
    
    transform = ResNet18_Weights.IMAGENET1K_V1.transforms()
    
    input_image = transform(img).unsqueeze(0) # Добавьте размерность пакета (batch dimension)
    
    device = torch.device("cuda" if torch.cuda.is_available() else 'mps')
    model.to(device)
    model.eval()
    input_image = input_image.to(device)
    #model.to(device)
    res=model(input_image).item()
    return f'Степень пёсости: {res}\n\n Т.е. это: {pet_map[round(res)]}'