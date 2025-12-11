import zlib
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

    def test_bad_payload_compressed_marker(self, serializer_factory):
        serializer = serializer_factory()
        payload = serializer.dump_payload({"id": 42})
        signed = serializer.make_signer().sign(b"." + payload)

        with pytest.raises(BadPayload) as exc_info:
            serializer.loads(signed)

        assert isinstance(exc_info.value.original_error, zlib.error)


class TestURLSafeTimedSerializer(TestURLSafeSerializer, TestTimedSerializer):
    @pytest.fixture()
    def serializer_factory(self):
        return partial(URLSafeTimedSerializer, secret_key="secret-key")
