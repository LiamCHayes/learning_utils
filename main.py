"""
Example of using this package
"""

## Import dlutils packages
from learning_utils import Memories
from learning_utils import DataTrackers

tracker = DataTrackers.TrainingLoopTracker('number', 'letter')

tracker.print_info()

tracker.update(1, 'a')
tracker.update(2, 'b')
tracker.update(1, 'a')

print(tracker.get_metrics_df())

