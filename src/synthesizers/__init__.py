from synthesizers.metgan import MeTGANSynthesizer

__all__ = (
    'MeTGANSynthesizer',
)


def get_all_synthesizers():
    return {
        name: globals()[name]
        for name in __all__
    }
