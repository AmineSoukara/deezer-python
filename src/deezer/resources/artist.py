from __future__ import annotations

from typing import TYPE_CHECKING

from ..pagination import PaginatedList
from .resource import Resource

if TYPE_CHECKING:
    from .album import Album
    from .playlist import Playlist
    from .track import Track


class Artist(Resource):
    """
    To work with Deezer artist objects.

    Check the :deezer-api:`Deezer documentation <artist>`
    for more details about each field.
    """

    id: int
    name: str
    link: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    nb_album: int
    nb_fan: int
    radio: bool
    tracklist: str

    def get_top(self, full=True, **kwargs) -> PaginatedList[Track]:
        """
        Get the top tracks of an artist.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Track <deezer.Track>` instances.
        """
        return self.get_paginated_list("top", **kwargs) if full else  self.get_relation("top", fwd_parent=False, **kwargs)

    def get_related(self, full=True, **kwargs) -> PaginatedList[Artist]:
        """
        Get a list of related artists.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Artist <deezer.Artist>` instances
        """
        return self.get_paginated_list("related", **kwargs) if full else  self.get_relation("related", fwd_parent=False, **kwargs)

    def get_radio(self, **kwargs) -> list[Track]:
        """
        Get a list of tracks.

        :returns: list of :class:`Track <deezer.Track>` instances
        """
        # radio returns tracks from different artists -> no fwd parent
        return self.get_relation("radio", fwd_parent=False, **kwargs)

    def get_albums(self, full=True, **kwargs) -> PaginatedList[Album]:
        """
        Get a list of artist's albums.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Album <deezer.Album>` instances
        """
        return self.get_paginated_list("albums", **kwargs) if full else  self.get_relation("albums", fwd_parent=False, **kwargs)

    def get_playlists(self, full=True, **kwargs) -> PaginatedList[Playlist]:
        """
        Get a list of artist's playlists.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Playlist <deezer.Playlist>` instances
        """
        return self.get_paginated_list("playlists", **kwargs) if full else  self.get_relation("playlists", fwd_parent=False, **kwargs)
