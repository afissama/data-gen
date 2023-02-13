from datagen.datagen import get_csv

features = {
    "Gender": {"Male": 150, "Female": 300, "Other": 50},
    "Religion": {"christ": 41, "muslim": 102, "athe": 41},
    "Race": {"black": 50, "white": 24, "asian": 100}
}

get_csv(500, features)
