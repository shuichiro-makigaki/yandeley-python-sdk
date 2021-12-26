from yandeley.models.groups import Group, GroupMember

from yandeley.resources.base import ListResource, GetByIdResource


class GroupsV2(GetByIdResource, ListResource):
    """
    Top-level resource for accessing groups.
    """
    _url = '/groups/v2'

    def __init__(self, session):
        self.session = session

    def get(self, id):
        """
        Retrieves a group by ID.

        :param id: the ID of the group to get.
        :return: a :class:`Group <yandeley.models.groups.Group>`.
        """
        return super(GroupsV2, self).get(id)

    def list(self, page_size=None):
        """
        Retrieves groups that the logged-in user is a member of, as a paginated collection.

        :param page_size: the number of groups to return on each page.  Defaults to 20.
        :return: a :class:`Page <yandeley.pagination.Page>` of :class:`GroupsV2 <yandeley.models.groups.Group>`.
        """
        return super(GroupsV2, self).list(page_size)

    def iter(self, page_size=None):
        """
        Retrieves groups that the logged-in user is a member of, as an iterator.

        :param page_size: the number of groups to retrieve at a time.  Defaults to 20.
        :return: an iterator of :class:`Groups <yandeley.models.groups.Group>`.
        """
        return super(GroupsV2, self).iter(page_size)

    @property
    def _session(self):
        return self.session

    def _obj_type(self, **kwargs):
        return Group


class GroupMembersV2(ListResource):
    """
    Resource for accessing members of a group.
    """
    def __init__(self, session, id):
        self.session = session
        self.id = id

    def list(self, page_size=None):
        """
        Retrieves members of the group, as a paginated collection.

        :param page_size: the number of members to return on each page.  Defaults to 20.
        :return: a :class:`Page <yandeley.pagination.Page>` of
                 :class:`GroupMembers <yandeley.models.groups.GroupMember>`.
        """
        return super(GroupMembersV2, self).list(page_size)

    def iter(self, page_size=None):
        """
        Retrieves members of the group, as an iterator.

        :param page_size: the number of members to retrieve at a time.  Defaults to 20.
        :return: an iterator of :class:`GroupMembers <yandeley.models.groups.GroupMember>`.
        """
        return super(GroupMembersV2, self).iter(page_size)

    @property
    def _session(self):
        return self.session

    def _obj_type(self, **kwargs):
        return GroupMember

    @property
    def _url(self):
        return '/groups/v2/%s/members' % self.id