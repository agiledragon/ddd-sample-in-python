from domain.service.cargo_service import CargoService


def create_cargo(cargo_id, after_days):
    CargoService().create(cargo_id, after_days)


def delay_cargo(cargo_id, days):
    CargoService().delay(cargo_id, days)


def get_cargo_after_days(cargo_id):
    return CargoService().get_after_days(cargo_id)


def destroy_cargo(cargo_id):
    CargoService().destroy(cargo_id)
