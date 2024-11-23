"""
    Hello and thanks for take a look at this script!
    This script contain AI,more accurate,we teach a Machine Learning with PYTORCH (TORCH library) to do some simple math additions,
additions with numbers from 1-10,with a small error(it will not say a 100% perfect/exact result)
    Follow @robert_de_romania on TikTok!
"""
import torch # The principal PYTORCH library,we need it to put the tensors(the tensors contain examples and correct answer)
import torch.nn as nn # We need it to create the model's 'brain' and loss function (the loss function say at the model how far is model's answer from correct answer)
import torch.optim as optim # We need this for optimize our model's answers (to make the model capable to learn)

# x_train contain the examples what the ML(Machine Learning)/model need to answer correct on the training loop
x_train = torch.tensor([[4,5],                       # 4 + 5
                        [9,0],                       # 9 + 0
                        [1,2],                       # 1 + 2
                        [3,1],                       # 3 + 1
                        [6,2]],dtype=torch.float32)  # 6 + 2

# y_train contain the correct answers for examples from x_train
y_train = torch.tensor([[9],[9],[3],[4],[8]],dtype=torch.float32) # 4 + 5 = 9 ; 9 + 0 = 9 ; 1 + 2 = 3 , ect

model = nn.Linear(2,1) # The model's 'brain' with a line of code,where this 'brain' take 2 inputs and generate a answer (1 output)
optimizer = optim.SGD(model.parameters(),lr=0.01) # The optimizer what optimize every loop the model's 'brain' to answer better next loop
loss_fn = nn.MSELoss() # The loss function what say at the model how far is model's answer from correct answer

for epoch in range(55): # The training loop
    y_pred = model(x_train) # The model's oppinion/prediction for every example from x_train
    loss = loss_fn(y_pred,y_train) # This say every loop how far is the model from correct answer (loss value cloosed from 0 is better)
    optimizer.zero_grad() # To not overfill the gardients number to learn correct
    loss.backward() 
    optimizer.step() # Apply the optimizer
    if epoch % 10 == 0: # Every 10 loops,show the current loss status
        print(f"Epoch: {epoch} , Loss: {loss}")

# Put personalized datas for example (test)
x = int(input())
y = int(input(f"{x} + "))

# The test with new example
x_test = torch.tensor([[x,y]],dtype=torch.float32)
y_test = model(x_test)

print(f"{x} + {y} = {y_test.item()}") # Show the test answer