import logging
from config.settings import settings


class RequireDebugFalse(logging.Filter):
  def filter(self, record):
    return not settings.APP_DEBUG


class RequireDebugTrue(logging.Filter):
  def filter(self, record):
    return settings.APP_DEBUG
