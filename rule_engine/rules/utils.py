import re

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type
        self.left = left
        self.right = right
        self.value = value

def create_ast_from_rule(rule_string):
    tokens = re.split(r'(\sAND\s|\sOR\s)', rule_string)
    root = None
    current_operator = None

    for token in tokens:
        token = token.strip()
        if token in ['AND', 'OR']:
            current_operator = Node(node_type='operator', value=token)
            if root is None:
                root = current_operator
        else:
            operand_node = Node(node_type='operand', value=token)
            if root:
                if current_operator.left is None:
                    current_operator.left = operand_node
                else:
                    current_operator.right = operand_node
                    root = current_operator
            else:
                root = operand_node

    return root

def evaluate_condition(condition, data):
    field, operator, value = re.split(r'(\s[<>]=?\s)', condition)
    field = field.strip()
    operator = operator.strip()
    value = value.strip()

    if value.isdigit():
        value = int(value)

    if operator == '>':
        return data[field] > value
    elif operator == '<':
        return data[field] < value
    elif operator == '>=':
        return data[field] >= value
    elif operator == '<=':
        return data[field] <= value
    elif operator == '=':
        return data[field] == value

    return False

def evaluate_ast(node, data):
    if node.node_type == 'operator':
        if node.value == 'AND':
            return evaluate_ast(node.left, data) and evaluate_ast(node.right, data)
        elif node.value == 'OR':
            return evaluate_ast(node.left, data) or evaluate_ast(node.right, data)
    elif node.node_type == 'operand':
        return evaluate_condition(node.value, data)

    return False

# Helper function to convert dictionary back to AST Node
def dict_to_node(node_dict):
    if node_dict is None:
        return None
    return Node(
        node_type=node_dict['node_type'],
        left=dict_to_node(node_dict['left']),
        right=dict_to_node(node_dict['right']),
        value=node_dict['value']
    )
