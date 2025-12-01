"""Agenticverse entity definition for the Stack Overflow replica."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

try:
  from agenticverse_entities.base.entity_base import BaseEntity  # type: ignore
except ImportError:  # pragma: no cover
  class BaseEntity:  # type: ignore
    """Minimal fallback so local runs do not fail."""

    name: str = ''

    def launch(self, *args: Any, **kwargs: Any):  # pylint: disable=unused-argument
      raise NotImplementedError('Agenticverse base Entity is unavailable.')

from metadata import StackoverflowReplicaMetadata
from server import start_server


@dataclass
class StackoverflowReplicaEntity(BaseEntity):
  """Expose the Stack Overflow replica to the Agenticverse runtime."""

  name: str = 'stackoverflow_replica'
  display_name: str = 'Stack Overflow Replica'
  description: str = 'Pixel-perfect recreation of stackoverflow.com/questions with dynamic injection.'
  metadata_schema = StackoverflowReplicaMetadata()

  def launch(self, port: int = 5000, threaded: bool = False, content_data: Optional[Dict[str, Any]] = None):
    """Start the Flask server and return the running application."""
    return start_server(port=port, threaded=threaded, content_data=content_data)
