def find_intersection(set_1, set_2):
    """
    计算第一个集合中每个框与第二个集合中每个框的交集面积

    :param set_1: 一个shape为[m,4]的tensor，代表m个边界坐标
    :param set_2: 一个shape为[n,4]的tensor，代表n个边界坐标
    :return: 一个shape为[m,n]的tensor，例如：[0,:]表示set_1中第1个框与set_2中每个框的交集面积
    """
    # max函数中的两个tensor的shape分别为[m,1,2], [1,n,2],可以应用广播机制，最后得到的tensor的shape为[m,n,2]
    # 例如：[0, :, 2]表示set_1中第一个框与set_2中所有框交集的左上角坐标
    lower_bounds = torch.max(set_1[:, :2].unsqueeze(1), set_2[:, :2].unsqueeze(0))  # [m, n, 2]
    # 计算右下角的坐标
    upper_bounds = torch.min(set_1[:, 2:].unsqueeze(1), set_2[:, 2:].unsqueeze(0))  # [m, n, 2]
    # 将两个减式小于0的设置为0
    intersection_dims = torch.clamp(upper_bounds - lower_bounds, min=0)  # [m, n, 2]
    # 相乘得到交集面积
    return intersection_dims[:, :, 0] * intersection_dims[:, :, 1]  # [m, n]


def find_jaccard_overlap(set_1, set_2):
    """
    计算第一个集合中每个框与第二个集合中每个框的Jaccard系数

    :param set_1: 一个shape为[m,4]的tensor，代表m个边界坐标
    :param set_2: 一个shape为[n,4]的tensor，代表n个边界坐标
    :return: 一个shape为[m,n]的tensor，例如：[0,:]表示set_1中第1个框与set_2中每个框的Jaccard系数
    """
    # 每个框与其他框的交集
    intersection = find_intersection(set_1, set_2)  # [m, n]

    # 计算每个集合中每个框的面积
    areas_set_1 = (set_1[:, 2] - set_1[:, 0]) * (set_1[:, 3] - set_1[:, 1])  # [m]
    areas_set_2 = (set_2[:, 2] - set_2[:, 0]) * (set_2[:, 3] - set_2[:, 1])  # [n]

    # 总面积减去交集就是并集
    # unsqueeze的作用同样是为了满足广播机制的条件
    union = areas_set_1.unsqueeze(1) + areas_set_2.unsqueeze(0) - intersection  # [m, n]
    # Jaccard系数 = 交集面积 / 并集面积
    return intersection / union  # [m, n]
