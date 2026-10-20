from main import attacks, dispatch


def test_untrusted_model_text_cannot_expand_trusted_permissions():
    for tool in ["EXPORT", "DELETE", "SEND"]:
        effects = []
        assert not dispatch(tool, True, effects)
        assert effects == []


def test_baseline_exposes_tool_misuse_and_search_remains_usable():
    effects = []
    assert dispatch("EXPORT", False, effects)
    assert dispatch("SEARCH", True, effects)
    assert not dispatch("INVALID", False, effects)
    assert len(attacks()) == 12
