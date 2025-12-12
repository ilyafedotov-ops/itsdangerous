import base64
from functools import partial

import pytest

from itsdangerous.exc import BadPayload
from itsdangerous.url_safe import URLSafeSerializer
from itsdangerous.url_safe import URLSafeTimedSerializer
from test_itsdangerous.test_serializer import TestSerializer
from test_itsdangerous.test_timed import TestTimedSerializer


class TestURLSafeSerializer(TestSerializer):
    @pytest.fixture()
    def serializer_factory(self):
        return partial(URLSafeSerializer, secret_key="secret-key")

    @pytest.fixture(params=({"id": 42}, pytest.param("a" * 1000, id="zlib")))
    def value(self, request):
        return request.param

    def test_load_payload_bad_compressed_data(self, serializer):
        bad_payload = b"." + base64.urlsafe_b64encode(b"not compressed").rstrip(b"=")

        with pytest.raises(BadPayload) as exc_info:
            serializer.load_payload(bad_payload)

        assert "zlib decompress" in str(exc_info.value)
        assert exc_info.value.original_error is not None


class TestURLSafeTimedSerializer(TestURLSafeSerializer, TestTimedSerializer):
    @pytest.fixture()
    def serializer_factory(self):
        return partial(URLSafeTimedSerializer, secret_key="secret-key")
