def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return list(sorted(artifacts, reverse=True,
                       key=lambda artifact: artifact['power']))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: ("* " + spell + " *"), spells))


def mage_stats(mages: list[dict]) -> dict:
    return {'max_power': max(mages, key=lambda mage: mage['power'])['power'],
            'min_power': min(mages, key=lambda mage: mage['power'])['power'],
            'avg_power': sum(map(lambda mage: mage['power'],
                                 mages)) / len(mages)}


def testing_artifact_sorter():
    print("Testing artifact sorter...")
    artifacts = [{'name': "over to", 'power': 703, 'type': "transport"},
                 {'name': "homo horder", 'power': 333, 'type': "atack"},
                 {'name': "Fire Staff", 'power': 92, 'type': "defance"},
                 {'name': "Crystal Orb", 'power': 85, 'type': "defance"}
                 ]
    try:
        srt_artifacts = artifact_sorter(artifacts)
        last = srt_artifacts[-1]
        before = srt_artifacts[-2]
        print(f"{before['name']} ({before['power']} power) comes before"
              f" {last['name']} ({last['power']} power)")
    except TypeError as e:
        print(e)
    except KeyError as e:
        print(e)
    except Exception as e:
        print(e)


def testing_spell_transformer():
    print("Testing spell transformer...")
    spells = ["andercover", "move on", "fireball", "heal", "shield"]

    try:
        for spell in spell_transformer(spells):
            print(spell, end=" ")
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)


def testing_power_filter():
    print("Testing power filter...")
    mages = [
        {'name': 'Gandalf', 'power': 100, 'element': 'light'},
        {'name': 'Saruman', 'power': 80, 'element': 'dark'},
        {'name': 'Radagast', 'power': 50, 'element': 'nature'},
        {'name': 'Alatar', 'power': 30, 'element': 'fire'}
    ]
    min_power = 60
    try:
        strong_mages = power_filter(mages, min_power)
        print(f"Mages with power >= {min_power}:")
        for mage in strong_mages:
            print(f"{mage['name']} ({mage['power']} power)")
    except TypeError as e:
        print(e)
    except KeyError as e:
        print(e)
    except Exception as e:
        print(e)


def testing_mage_stats():
    print("Testing mage stats...")
    mages = [
        {'name': 'Gandalf', 'power': 100, 'element': 'light'},
        {'name': 'Saruman', 'power': 80, 'element': 'dark'},
        {'name': 'Radagast', 'power': 50, 'element': 'nature'},
        {'name': 'Alatar', 'power': 30, 'element': 'fire'}
    ]
    try:
        stats = mage_stats(mages)
        print(f"Max power: {stats['max_power']}")
        print(f"Min power: {stats['min_power']}")
        print(f"Avg power: {stats['avg_power']}")
    except TypeError as e:
        print(e)
    except KeyError as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    testing_artifact_sorter()
    print()
    testing_spell_transformer()
    print(end="\n\n")
    testing_power_filter()
    print()
    testing_mage_stats()
