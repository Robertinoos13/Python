import torch
import torch.nn as nn
import torch.optim as optim

# RAM, ROM, nm at chipset, 3/4/5G, Hz, camera resolution, batery mAh, year when was rated
input_train = torch.tensor([[4,128,12,4,90,1080,4300,2024],
                            [8,256,6,4,120,2160,5000,2025],
                            [6,256,8,5,60,1080,4500,2024],
                            [2,32,16,4,60,720,3000,2024],
                            [12,512,4,5,120,4320,5000,2024],
                            [8,256,4,5,120,2160,5000,2024],
                            [8,256,4,5,120,2160,5000,2020],
                            [2,32,16,4,60,720,3000,2000],
                            [12,512,4,5,120,4320,5000,2050],
                            [4,128,12,4,90,1080,4300,2015],
                            [32,2048,1,7,240,8640,8000,2033],
                            [12,1024,4,3,144,4320,5000,2022],
                            [12,1024,4,3,144,4320,5000,2014],
                            [4,16,18,3,60,1080,3500,2014],
                            [2,16,28,3,60,1080,2500,2014],
                            [3,32,14,4,60,1080,3000,2016],
                            [4,64,10,4,90,1080,3500,2019],
                            [6,128,7,5,120,2160,4000,2021],
                            [12,256,5,5,120,4320,5000,2022],
                            [4,256,7,4,60,2160,3200,2019],
                            [4,256,7,4,60,2160,3200,2025],
                            [1,32,45,3,60,720,1500,2010],
                            [1,32,45,3,60,720,1500,2025],
                            [4,64,12,4,60,1080,4000,2020],
                            [4,64,12,4,60,1080,4000,2025],
                            [2,8,28,4,60,720,2600,2016],
                            [2,8,28,4,60,720,2600,2025],
                            [16,1024,3,5,120,4320,5000,2025],
                            [2,32,14,4,60,1080,3400,2019],
                            [6,64,10,4,60,2160,3300,2018],
                            [6,128,8,4,90,2160,4500,2021],
                            [8,256,6,4,120,2160,5000,2025],
                            [6,64,7,4,90,2160,2800,2019],
                            [8,128,5,5,120,2160,4600,2021],
                            [6,128,8,4,60,2160,4500,2020],
                            [3,32,12,4,60,1080,5000,2020],
                            [4,64,12,4,60,1080,3500,2019],
                            [16,1024,3,5,240,4320,6000,2025],
                            [6,128,12,4,90,1080,4000,2019],
                            [12,512,5,5,144,2160,6000,2025],
                            [8,256,10,5,120,1080,4000,2021],
                            [12,512,5,5,144,4320,6000,2025],
                            [24,2048,2,3,240,4320,5000,2025],
                            [2,16,28,3,60,1080,2500,2023],
                            [1,4,45,3,30,480,1000,2015],
                            [1,4,32,3,60,720,1500,2012],
                            [2,32,28,4,60,1080,3000,2016],
                            [4,128,10,5,90,1080,4500,2025],
                            [2,16,28,3,60,720,2500,2014],
                            [3,32,22,3,60,720,3000,2017],
                            [4,64,18,3,60,1080,3500,2015],
                            [6,256,7,5,120,1080,5000,2024],
                            [6,64,14,4,90,1080,3500,2017],
                            [6,128,10,4,120,2160,4000,2020],
                            [8,128,12,5,120,1080,4500,2021],
                            [1,2,65,3,30,480,1000,1900],
                            [1,2,65,3,30,480,1000,2008],
                            [1,2,65,3,30,480,1000,2010],
                            [1,2,65,3,30,480,1000,2011],
                            [1,2,65,3,30,480,1000,2012],
                            [1,4,65,3,30,480,1000,1990],
                            [1,4,65,3,30,480,1000,2009],
                            [1,4,65,3,30,480,1000,2011],
                            [1,4,65,3,30,480,1000,2013],
                            [1,4,65,3,30,480,1000,2015],
                            [1,4,65,4,60,720,1000,2000],
                            [1,4,65,4,60,720,1000,2012],
                            [1,4,65,4,60,720,1000,2013],
                            [1,4,65,4,60,720,1000,2015],
                            [1,4,65,4,60,720,1000,2016],
                            [1,4,48,4,60,720,3000,2000],
                            [1,4,48,4,60,720,3000,2015],
                            [1,4,48,4,60,720,3000,2018],
                            [1,4,48,4,60,720,3000,2019],
                            [1,4,48,4,60,720,3000,2020],
                            [6,8,12,5,60,1080,5000,2010],
                            [6,8,12,5,60,1080,5000,2017],
                            [6,8,12,5,60,1080,5000,2018],
                            [6,8,12,5,60,1080,5000,2019],
                            [6,8,12,5,60,1080,5000,2020],
                            [6,64,12,5,60,1080,5000,2010],
                            [6,64,12,5,60,1080,5000,2020],
                            [6,64,12,5,60,1080,5000,2022],
                            [6,64,12,5,60,1080,5000,2023],
                            [6,64,12,5,60,1080,5000,2024],
                            [8,256,6,4,120,2160,5000,2016],
                            [8,256,4,5,120,2160,5000,2024],
                            [3,128,12,4,60,1080,5020,2020],
                            [2,32,12,4,60,1080,3020,2019],
                            [8,256,6,3,120,2160,5000,2024],
                            [1,2,90,3,60,480,3300,2000],
                            [1,2,90,3,60,480,3300,2005],
                            [1,2,90,3,60,480,3300,2008],
                            [1,2,90,3,60,480,3000,2011],
                            [1,2,90,3,60,480,3000,2014],
                            [8,256,6,4,120,2160,5000,2018],
                            [8,256,6,4,120,2160,5000,2020],
                            [8,256,6,4,120,2160,5000,2023],
                            [4,128,8,4,90,1080,4500,2025],
                            [8,256,90,4,120,2160,5000,2025],
                            [1,2,60,3,240,480,2000,1],
                            [16,512,4,5,120,2160,5000,2023],
                            [16,512,4,5,120,2160,5000,2027],
                            [16,512,4,5,120,2160,5000,2030],
                            [16,512,4,5,120,2160,5000,2035],
                            [1,1,90,3,30,360,1000,1],
                            [6,256,5,5,60,2160,3687,2022],
                            [6,256,5,5,60,2160,3687,2026],
                            [6,256,5,5,60,2160,3687,2030],
                            [32,2048,90,5,240,8640,99,2024],],dtype=torch.float32)

# 1-Low End, 2-Mid entry Level, 3-Mid Range, 4-Mid Superior, 5-High End
output_train = torch.tensor([[2],[3],[2],[1],[5],[4],[5],[5],[1],[5],[5],[1],[5],[3],[1],[2],[3],[4],[5],[5],[3],[5],[1],[3],[1],[2],[1],[5],[2],[4],[4],[3],[4],[4],[4],[2],[2],[5],[4],[4],[4],[4],[1],[1],[1],[1],[2],[2],[2],[2],[3],[3],[3],[3],[3],[5],[4],[3],[2],[1],[5],[4],[3],[2],[1],[5],[4],[3],[2],[1],[5],[4],[3],[2],[1],[5],[4],[3],[2],[1],[5],[4],[3],[2],[1],[5],[4],[3],[2],[1],[5],[4],[3],[2],[1],[5],[4],[3],[2],[1],[5],[4],[3],[2],[1],[5],[4],[3],[2],[1]],dtype=torch.float32)

def print_line():
    print("-----------")

def normalize_datas(current_input):
    normalized_input = current_input.clone()
    for i in range(len(normalized_input)):
        normalized_input[i, 0] /= 32  # RAM
        normalized_input[i, 1] /= 2048  # ROM
        normalized_input[i, 2] /= 90  # nm
        normalized_input[i, 3] /= 5  # G
        normalized_input[i, 4] /= 240  # Hz
        normalized_input[i, 5] /= 8640  # Camera resolution
        normalized_input[i, 6] /= 9999  # Battery
        normalized_input[i, 7] = (normalized_input[i, 7] - 2000) / 50  # Year
    return normalized_input

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.l1 = nn.Linear(8, 128)
        self.a1 = nn.ReLU()
        self.l2 = nn.Linear(128, 64)
        self.a2 = nn.ReLU()
        self.l3 = nn.Linear(64, 32)
        self.a3 = nn.ReLU()
        self.l4 = nn.Linear(32, 16)
        self.a4 = nn.ReLU()
        self.l5 = nn.Linear(16, 8)
        self.a5 = nn.ReLU()
        self.l6 = nn.Linear(8, 1)
    
    def forward(self, x):
        x = normalize_datas(x)  # Normalize the datas
        x = self.a1(self.l1(x))
        x = self.a2(self.l2(x))
        x = self.a3(self.l3(x))
        x = self.a4(self.l4(x))
        x = self.a5(self.l5(x))
        x = self.l6(x)
        x = torch.clamp(x, min=0.0, max=5.5)
        return x 
    
model = Model()
loss_fn = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for i in range(2001):
    y_pred = model(input_train)
    loss = loss_fn(y_pred, output_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if i % 50 == 0:
        print(f"Epoch: {i}; Loss: {loss:.5f}")

if __name__ == "__main__":
    def rate_final_output():
        global output_test
        if output_test > 0 and output_test < 1.5:
            final_output = "Low End"
        elif output_test > 1.5 and output_test < 2.5:
            final_output = "Mid Entry Level"
        elif output_test > 2.5 and output_test < 3.5:
            final_output = "Mid Range"
        elif output_test > 3.5 and output_test < 4.5:
            final_output = "Mid Superior"
        elif output_test > 4.5 and output_test < 5.51:
            final_output = "High End"
        else:
            final_output = f"I cant to rate this phone,because my prediction is not between 0 and 5.5 (My final prediction: {output_test.item():.1f})"

        return final_output
    
    # Quick direct testing (20 tests)
    input_test = torch.tensor([[8, 256, 6, 4, 120, 2160, 5000, 2025]], dtype=torch.float32) # Redmi Note 13 Pro 4G scecs in 2025
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"\nRedmi Note 13 Pro 4G in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: Mid Range)")
    print(output_test.item())
    print_line()
    
    input_test = torch.tensor([[4, 64, 12, 4, 60, 1080, 4000, 2020]], dtype=torch.float32) # HUAWEI P smart Z specs in 2020
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"HUAWEI P smart Z in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: Mid Range)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[12, 512, 4, 5, 120, 4320, 5000, 2025]], dtype=torch.float32) # Samsung S24 Ultra specs in 2025
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"Samsung S24 Ultra in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: High End)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[16, 512, 4, 5, 120, 4320, 4700, 2022]], dtype=torch.float32) # Google Pixel 9 Pro specs in 2022
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"Google Pixel 9 Pro in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: High End)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[1, 8, 4, 4, 60, 720, 2000, 2020]], dtype=torch.float32) # Samsung J2 specs in 2020
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"Samsung J2 in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: Low End)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[8, 256, 6, 4, 120, 2160, 5000, 2011]], dtype=torch.float32) # Redmi Note 13 Pro 4G scecs in 2011
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"Redmi Note 13 Pro 4G in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: High End)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[4, 64, 12, 4, 60, 1080, 4000, 2025]], dtype=torch.float32) # HUAWEI P smart Z specs in 2025
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"HUAWEI P smart Z in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: Low End)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[12, 512, 4, 5, 120, 4320, 5000, 2015]], dtype=torch.float32) # Samsung S24 Ultra specs in 2015
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"Samsung S24 Ultra in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: High End)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[16, 512, 4, 5, 120, 4320, 4700, 2025]], dtype=torch.float32) # Google Pixel 9 Pro specs in 2025
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"Google Pixel 9 Pro in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: High End)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[1, 8, 4, 4, 60, 720, 2000, 2015]], dtype=torch.float32) # Samsung J2 specs in 2015
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"Samsung J2 in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: Mid Entry Level)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[8, 256, 6, 4, 120, 2160, 4300, 2022]], dtype=torch.float32) # HUAWEI Nova 9 specs in 2022
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"HUAWEI Nova 9 in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: Mid Range)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[8, 256, 6, 4, 120, 2160, 4300, 2025]], dtype=torch.float32) # HUAWEI Nova 9 specs in 2025
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"HUAWEI Nova 9 in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: Mid Range)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[6, 512, 5, 5, 60, 2160, 3687, 2020]], dtype=torch.float32) # iPhone 12 Pro Max specs in 2020
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"iPhone 12 Pro Max in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: High End)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[6, 512, 5, 5, 60, 2160, 3687, 2025]], dtype=torch.float32) # iPhone 12 Pro Max specs in 2025
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"iPhone 12 Pro Max in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: Mid Range)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[12, 1024, 7, 4, 60, 2160, 4100, 2019]], dtype=torch.float32) # Samsung S10+ specs in 2019
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"Samsung S10+ in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: High End)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[12, 1024, 7, 4, 60, 2160, 4100, 2025]], dtype=torch.float32) # Samsung S10+ specs in 2025
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"Samsung S10+ in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: Mid Range)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[12, 256, 4, 5, 120, 2160, 5000, 2025]], dtype=torch.float32) # Samsung A56 specs in 2025
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"Samsung A56 in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: Mid Superior)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[12, 256, 4, 5, 120, 2160, 5000, 2020]], dtype=torch.float32) # Samsung A56 specs in 2020
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"Samsung A56 in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: High End)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[4, 128, 12, 4, 60, 1080, 5000, 2022]], dtype=torch.float32) # Samsung A03 specs in 2022
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"Samsung A03 in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: Mid Entry Level)")
    print(output_test.item())
    print_line()

    input_test = torch.tensor([[4, 128, 12, 4, 60, 1080, 5000, 2025]], dtype=torch.float32) # Samsung A03 specs in 2025
    normalize_datas(input_test)
    output_test = model(input_test)
    print(f"Samsung A03 in {int(input_test[0, 7])}: {rate_final_output()} (correct answer: Low End)")
    print(output_test.item())
    print_line()