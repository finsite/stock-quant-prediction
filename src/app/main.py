"""Main entry point for the stock-quant-prediction module.

Initializes the prediction engine, sets up logging,
and begins consuming messages for model-based prediction.
"""

import os
import sys

# Add 'src/' to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.utils.setup_logger import setup_logger
from app.queue_handler import consume_messages

# Initialize logger
logger = setup_logger(__name__)


def main() -> None:
    """Starts the prediction engine service.

    This service consumes feature data from the message queue,
    applies a predictive model (e.g., regression, LSTM),
    and publishes forecasted outputs.
    """
    logger.info("🚀 Starting Prediction Engine Service...")
    consume_messages()


if __name__ == "__main__":
    main()
