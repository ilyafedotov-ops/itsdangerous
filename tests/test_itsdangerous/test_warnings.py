import warnings


def test_runtime_warning_is_allowed():
    # QA downgrade: warnings should be visible but not treated as errors.
    warnings.warn("runtime warnings remain non-fatal during tests", UserWarning)
