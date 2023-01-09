import ast


class BinOpLister(ast.NodeVisitor):
    def visit_BinOp(self, node):
        print(f'left: {node.left}')
        print(f'op: {node.op}')
        print(f'right: {node.right}')
        self.generic_visit(node)


def the_ast():
    expression = "1 + 2"
    tree = ast.parse(expression)
    print(ast.dump(tree))


def parse_ast(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contents = file.read()
        tree = ast.parse(contents)

    for n in tree.body:
        print(n, n.lineno, n.end_lineno)
        BinOpLister().visit(n)
    print()

    # nodes = ast.walk(tree)
    # for n in nodes:
    #     print(n)
    # print()


def eval_input():
    user_input = "5"
    print(type(user_input))

    check_user_input = ast.literal_eval(user_input)
    print(type(check_user_input))


def parse_ast_args(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contents = file.read()
        tree = ast.parse(contents)

    print(ast.dump(tree))
    print()
    function1 = tree.body[1]
    function2 = tree.body[2]
    args1 = [a.arg for a in function1.args.args]
    args2 = [a.arg for a in function2.args.args]
    print(args1)
    print(args2)


def parse_ast_tree_walk(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contents = file.read()
        tree = ast.parse(contents)

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            print(f'Function name: {function_name}')
            # check whether the function's name is written in camel_case
            for fn_node in ast.walk(node):
                if isinstance(fn_node, ast.Assign):
                    target_name = fn_node.targets[0].id
                    print(f'FN Assign name: {target_name}')
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            print(f'Class name: {class_name}')
        if isinstance(node, ast.Assign):
            target_name = node.targets[0].id
            print(f'Assign name: {target_name}')



if __name__ == '__main__':
    # the_ast()
    # parse_ast('assert.py')
    # eval_input()
    # parse_ast_args('assert.py')

    # parse_ast_tree_walk('assert.py')
    # parse_ast_tree_walk('classes.py')

    parse_ast_tree_walk('../supplemental/code-analyzer/test4.py')
