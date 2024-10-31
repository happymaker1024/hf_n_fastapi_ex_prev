# True면 GPU 사용 가능
import torch
print(torch.cuda.is_available())

# GPU 사용 여부 확인
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Using device: {device}')