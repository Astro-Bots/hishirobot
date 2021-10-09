import os

suffix = os.getenv("SUFFIX", "")

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'+suffix
        self.mirCommand = 'mir'+suffix
        self.UnzipmirCommand = 'unzipmir'+suffix
        self.ZipmirCommand = 'zipmir'+suffix
        self.Cancelmir = 'cancel'+suffix
        self.CancelAllCommand = 'cancelall'+suffix
        self.SearchCommand = 'search'+suffix
        self.StatusCommand = 'status'+suffix
        self.AuthorizedUsersCommand = 'users'+suffix
        self.AuthorizeCommand = 'auth'+suffix
        self.UnAuthorizeCommand = 'unauth'+suffix
        self.AddSudoCommand = 'addsudo'+suffix
        self.RmSudoCommand = 'rmsudo'+suffix
        self.PingCommand = 'ping'+suffix
        self.RestartCommand = 'restart'+suffix
        self.StatsCommand = 'stats'+suffix
        self.HelpCommand = 'help'+suffix
        self.LogCommand = 'log'+suffix
        self.SpeedCommand = 'speedtest'+suffix
        self.CloneCommand = 'clone'+suffix
        self.CountCommand = 'count'+suffix
        self.WatchCommand = 'watch'+suffix
        self.RebootCommand = 'reboot'+suffix
        self.ShutDownCommand = 'shutdown'+suffix
        self.ZipWatchCommand = 'zipwatch'+suffix
        self.QbmirCommand = 'qbmir'+suffix
        self.QbUnzipmirCommand = 'qbunzipmir'+suffix
        self.QbZipmirCommand = 'qbzipmir'+suffix
        self.DeleteCommand = 'del'+suffix
        self.ShellCommand = 'sh'+suffix
        self.ExecHelpCommand = 'exechelp'+suffix
        self.RssHelpCommand = 'rsshelp'+suffix
        self.LeechSetCommand = 'leechset'+suffix
        self.SetThumbCommand = 'setthumb'+suffix
        self.LeechCommand = 'leech'+suffix
        self.UnzipLeechCommand = 'unzipleech'+suffix
        self.ZipLeechCommand = 'zipleech'+suffix
        self.QbLeechCommand = 'qbleech'+suffix
        self.QbUnzipLeechCommand = 'qbunzipleech'+suffix
        self.QbZipLeechCommand = 'qbzipleech'+suffix
        self.LeechWatchCommand = 'leechwatch'+suffix
        self.LeechZipWatchCommand = 'leechzipwatch'+suffix

BotCommands = _BotCommands()
