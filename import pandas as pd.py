import pandas as pd
data_frame1 = pd.DataFrame({
    'Fruits': ['Apple', 'Banana', 'Mango', 'Dragon Fruit', 'Musk melon', 'Grapes'],
    'Sales in kg': [20, 30, 15, 10, 50, 40]
})

data_frame2 = pd.DataFrame({
    'Vegetables': ['Beans', 'Bedroot', 'Carrot'],
    'Sales in kg': [200, 310, 115]
})

data_frame3 = pd.DataFrame({
    'Baked Items': ['Rusk', 'Puffs', 'Cupcakes'],
    'Sales in kg': [55, 45, 30]
})
with pd.ExcelWriter(r'C:\Users\eliances\Desktop\file_register\file.xlsx', engine='openpyxl') as writer:
    data_frame1.to_excel(writer, sheet_name='Fruits', index=False)
    data_frame2.to_excel(writer, sheet_name='Vegetables', index=False)
    data_frame3.to_excel(writer, sheet_name='Baked Items', index=False)
#data_frame4 = pd.DataFrame({
 #   'Cool Drinks': ['Miranda', '7up', 'Sprite'],
  #  'Sales in kg': [100, 150, 200]
#})

#with pd.ExcelWriter("path_to_file.xlsx", mode='a', engine='openpyxl') as writer:
 #   data_frame4.to_excel(writer, sheet_name='Cool Drinks', index=False)
