import pytest
from src.entity.Task import Task


class TestEntity:

    @pytest.fixture(scope="function")
    def stub_entity(self) -> Task:
        task = Task(id=1, title="test", description="test", category="test", date_exp="2020-01-01",
                    priority="test", status="test")
        return task

    def test_entity_repr(self, stub_entity: Task):
        repr_format = (f"Task(id={stub_entity.id}, title={stub_entity.title}, description={stub_entity.description}, "
                       f"category={stub_entity.category}, data_exp={stub_entity.date_exp}, priority={stub_entity.priority})")
        assert repr_format == stub_entity.__repr__()
