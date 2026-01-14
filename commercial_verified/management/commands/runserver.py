"""
Custom runserver command that displays a custom startup message
"""
from django.core.management.commands.runserver import Command as RunserverCommand
from django.utils.autoreload import get_reloader


class Command(RunserverCommand):
    """
    Override the default runserver command to show custom startup message
    """
    
    def inner_run(self, *args, **options):
        """
        Override inner_run to customize the startup message
        """
        # Get the address and port
        if options.get('addrport'):
            addrport = options['addrport']
        else:
            addrport = self.default_addr + ':' + str(self.default_port)
        
        # Customize the startup message
        self.stdout.write(
            self.style.SUCCESS(
                f'\n🚀 Starting commercial_verified app at http://{addrport}/'
            )
        )
        self.stdout.write(
            self.style.WARNING(
                'Quit the server with CONTROL-C.\n'
            )
        )
        
        # Call parent inner_run to actually start the server
        # The parent will still print its message, but ours comes first
        super().inner_run(*args, **options)
