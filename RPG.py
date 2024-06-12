class SkillNode:
    def __init__(self, name):
        self.name = name
        self.sub_skills = []

    def add_sub_skill(self, sub_skill):
        if len(self.sub_skills) < 2:
            self.sub_skills.append(sub_skill)
            return True
        else:
            print(f"Erro: Não é possível adicionar mais de 2 sub-habilidades ao nó {self.name}")
            return False

    def __repr__(self):
        return self.name

class SkillTree:
    def __init__(self):
        self.root = SkillNode("Root")

    def is_valid_path(self, path):
        current = self.root
        for part in path:
            found = False
            for sub_skill in current.sub_skills:
                if sub_skill.name == part:
                    current = sub_skill
                    found = True
                    break
            if not found:
                return False
        return True

    def add_skill(self, path, skill_name):
        current = self.root
        for part in path:
            for sub_skill in current.sub_skills:
                if sub_skill.name == part:
                    current = sub_skill
                    break
        new_skill = SkillNode(skill_name)
        return current.add_sub_skill(new_skill)

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
            half = len(node.sub_skills) // 2
            for i, sub_skill in enumerate(node.sub_skills):
                if i == half:
                    print("  " * level + node.name)
                self.display(sub_skill, level + 1)
        else:
            print("  " * level + node.name)
            for sub_skill in node.sub_skills:
                self.display(sub_skill, level + 1)

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def display(self):
        print("Inventário:", self.items)

class Character:
    def __init__(self, name):
        self.name = name
        self.skill_tree = SkillTree()
        self.inventory = Inventory()

    def add_skill(self, path, skill_name):
        return self.skill_tree.add_skill(path, skill_name)

    def add_item_to_inventory(self, item):
        self.inventory.add_item(item)

    def display_skills(self):
        print(f"\nÁrvore de Habilidades de {self.name}:")
        self.skill_tree.display()

    def display_inventory(self):
        print(f"\nInventário de {self.name}:")
        self.inventory.display()

def create_character():
    name = input("Digite o nome do personagem: ")
    return Character(name)

def add_skills(character):
    while True:
        skill_path = input("\nDigite o caminho para a habilidade (separado por espaços, vazio para raiz): ").split()
        if not character.skill_tree.is_valid_path(skill_path):
            print(f"\nErro: O caminho {' > '.join(skill_path)} não existe. Adicione um caminho válido.")
            character.display_skills()
            continue
        skill_name = input("Digite o nome da habilidade: ")
        success = character.add_skill(skill_path, skill_name)
        if success:
            print("\nHabilidade adicionada com sucesso.")
        character.display_skills()
        cont = input("\nDeseja adicionar outra habilidade? (s/n): ")
        if cont.lower() != 's':
            break

def add_items(character):
    while True:
        item_name = input("Digite o nome do item: ")
        character.add_item_to_inventory(item_name)
        cont = input("Deseja adicionar outro item? (s/n): ")
        if cont.lower() != 's':
            break

if __name__ == "__main__":
    character = create_character()
    print(f"\nPersonagem {character.name} criado com sucesso!")

    print("\nVamos adicionar habilidades:")
    add_skills(character)

    print("\nVamos adicionar itens ao inventário:")
    add_items(character)

    print("\nExibindo a árvore de habilidades:")
    character.display_skills()

    print("\nExibindo o inventário:")
    character.display_inventory()