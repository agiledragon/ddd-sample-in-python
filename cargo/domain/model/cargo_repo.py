from domain.model.base.repo import Repo


_caro_repo = Repo()


def set_cargo_repo(repo):
    global _caro_repo
    _caro_repo = repo


def get_cargo_repo():
    return _caro_repo


