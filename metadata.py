"""Metadata schema for the Stack Overflow replica entity."""

from __future__ import annotations

try:
  from agenticverse_entities.base.metadata_base import BaseMetadata, Metadata  # type: ignore
except ImportError:  # pragma: no cover
  class Metadata(dict):  # type: ignore
    """Fallback metadata container."""

    def __init__(self, domain: str, parameters: dict):
      super().__init__(domain=domain, parameters=parameters)

  class BaseMetadata:  # type: ignore
    def get_metadata(self) -> Metadata:  # pragma: no cover
      raise NotImplementedError


class StackoverflowReplicaMetadata(BaseMetadata):
  """Describe the parameters the replica accepts for dynamic content."""

  def get_metadata(self) -> Metadata:
    return Metadata(
        domain='*.stackoverflow.com',
        parameters={
            'port': 'integer',
            'section': 'string',
            'title': 'string',
            'excerpt': 'string',
            'description': 'string',
            'user': 'string',
            'author': 'string',
            'votes': 'integer',
            'answers': 'integer',
            'views': 'integer',
            'answered': 'boolean',
            'tags': 'array',
            'badge': 'string',
            'date': 'string',
            'url': 'string',
        },
    )
