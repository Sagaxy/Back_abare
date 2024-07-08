from logs.logger import Logger
from utils.mock_data_loader import read_mock_data
from models.classgroups import ChildAbbreviated, ClassGroupWithChildren, ClassGroupsWithChildren


class ClassGroupsController:
    def __init__(self, logger: Logger = None) -> None:
        """
        Initialize the users controller
        """
        if logger:
            self.logger = logger
            self.logger.info("Users controller instance created.")

    def get_classgroups_with_children(self) -> ClassGroupsWithChildren:
        """
        Get brief information about all classgroups with its given children
        """
        self.logger.info("Reading classgroups with given children in it")
        children_data = read_mock_data("children.json", logger=self.logger)
        class_groups_data = read_mock_data("classgroups.json", logger=self.logger)
        class_groups = []
        for class_group_data in class_groups_data["classgroups"]:
            children_in_class_group = []
            for child_data in children_data["children"]:
                if child_data["classgroup"] == class_group_data["id"]:
                    child = ChildAbbreviated(child_data)
                    children_in_class_group.append(child)
            class_groups.append(ClassGroupWithChildren(class_group_data, children_in_class_group))
        return ClassGroupsWithChildren(class_groups)