import random


class Prescription:
    medication_list = ["Ибупрофен", "Леводопа", "Амоксициллин", "Эритромицин", "Тамоксифен", "Варфарин"]
    recipe_templates = []

    def __init__(self, disease, prescribed_medicine):
        self.disease = disease
        self.prescribed_medicine = prescribed_medicine
        self.generateRecipe()

    def generateRecipe(self):
        recipe_id = random.randint(1000, 9999)
        recipe = {"Болезнь": self.disease, "Лекарство": self.prescribed_medicine, "Идентификатор рецепта": recipe_id}
        if self.prescribed_medicine not in Prescription.medication_list:
            Prescription.medication_list.append(self.prescribed_medicine)
            Prescription.recipe_templates.append(recipe)
        else:
            Prescription.recipe_templates.append(recipe)
        return recipe

    @classmethod
    def getRecipe(cls):
        for recipe in cls.recipe_templates:
            print(recipe)


print('Список лекарств:', Prescription.medication_list) # Начальный список лекарств
rec1 = Prescription('Грип', 'Амоксициллин')
print('Первый рецепт:', Prescription.recipe_templates) # Не добавлен, т.к. лекарство - в списке
rec2 = Prescription('Грип', 'Ацикловир')
print('Второй рецепт:', Prescription.recipe_templates) # Добавлен, т.к. лекарства нет в списке
rec3 = Prescription('Волчанка', 'Азатиоприн')
print('Третий рецепт:', Prescription.recipe_templates) # Добавлен, т.к. лекарства нет в списке
rec4 = Prescription('Имунодифицит', 'Азатиоприн')
print('Четвертый рецепт:', Prescription.recipe_templates) # Не добавлен, т.к. лекарство - в списке
print('Список лекарств:', Prescription.medication_list) # Конечный список лекарств
Prescription.getRecipe()






