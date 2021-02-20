import networkx as nx

if __name__ == '__main__':
    with open("edges.txt") as input:
        edges_list = [(int(line.split()[0]), int(line.split()[1])) for line in input.readlines()]
    graph = nx.Graph(edges_list)
    print("1. Количество ребер - {}.".format(graph.number_of_edges()))
    print("2. Количество изолятов - {}.".format(len(list(nx.isolates(graph)))))
    if len(list(nx.isolates(graph))) != 0:
        print("Изоляты - {}.".format(list(nx.isolates(graph))))
    node = max(graph.degree, key=lambda x: x[1])
    print("3. Вершина с самой большой стпенью - {}. Ее степень равна {}".
          format(node[0], node[1]))
    component = nx.Graph(graph)
    component.remove_nodes_from(nx.isolates(graph))
    print("4. Диаметр графа - {}".format(nx.diameter(component)))
    try:
        ab_path = nx.shortest_path(graph, 632, 471)
    except nx.NetworkXNoPath:
        print("5. Между А и B нет пути.")
    else:
        print("5. Кратчайший путь от A до B:\nЕго длина - {}, "
              "последовательность вершин - {}.".format(len(ab_path), ab_path))
    try:
        cd_path = nx.shortest_path(graph, 911, 325)
    except nx.NetworkXNoPath:
        print("6. Между C и D нет пути.")
    else:
        print("6. Кратчайший путь от C до D:\nЕго длина - {}, "
              "последовательность вершин - {}.".format(len(cd_path), cd_path))
    try:
        ef_path = nx.shortest_path(graph, 162, 965)
    except nx.NetworkXNoPath:
        print("7. Между E и F нет пути.")
    else:
        print("7. Кратчайший путь от C до D:\nЕго длина - {}, "
              "последовательность вершин - {}.".format(len(ef_path), ef_path))

    graph.remove_nodes_from([512, 68, 709, 357, 778, 626, 469, 278])

    print("8. Количество ребер - {}.".format(graph.number_of_edges()))
    print("9. Количество изолятов - {}.".format(len(list(nx.isolates(graph)))))
    if len(list(nx.isolates(graph))) != 0:
        print("Изоляты - {}.".format(list(nx.isolates(graph))))
    node = max(graph.degree, key=lambda x: x[1])
    print("10. Вершина с самой большой стпенью - {}. Ее степень равна {}".
          format(node[0], node[1]))
    component = nx.Graph(graph)
    component.remove_nodes_from(nx.isolates(graph))
    print("11. Диаметр графа - {}".format(nx.diameter(component)))
    try:
        ab_path = nx.shortest_path(graph, 632, 471)
    except nx.NetworkXNoPath:
        print("12. Между А и B нет пути.")
    else:
        print("12. Кратчайший путь от A до B:\nЕго длина - {}, "
              "последовательность вершин - {}.".format(len(ab_path), ab_path))
    try:
        cd_path = nx.shortest_path(graph, 911, 325)
    except nx.NetworkXNoPath:
        print("13. Между C и D нет пути.")
    else:
        print("13. Кратчайший путь от C до D:\nЕго длина - {}, "
              "последовательность вершин - {}.".format(len(cd_path), cd_path))
    try:
        ef_path = nx.shortest_path(graph, 162, 965)
    except nx.NetworkXNoPath:
        print("14. Между E и F нет пути.")
    else:
        print("14. Кратчайший путь от C до D:\nЕго длина - {}, "
              "последовательность вершин - {}.".format(len(ef_path), ef_path))
