from datagen.datagen import get_csv

features = {
    "Gender": {"Male": 14, "Female": 60, "Other": 40},
    "Religion": {"christ": 41, "muslim": 102, "athe": 41},
    "Race": {"black": 50, "white": 24, "asian": 100}
}

get_csv(100, features)
