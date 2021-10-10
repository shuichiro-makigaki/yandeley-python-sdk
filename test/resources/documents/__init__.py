import arrow

from yandeley.models import Person
from test import load_config, get_user_session


def __delete_all(doc_resource):
    for doc in doc_resource.iter():
        doc.delete()


def delete_all_documents():
    config = load_config()
    if config['recordMode'] != 'none':
        session = get_user_session()
        __delete_all(session.documents)
        __delete_all(session.trash)


def delete_all_group_documents():
    config = load_config()
    if config['recordMode'] != 'none':
        session = get_user_session()
        group = session.groups.get('164d48fb-2343-332d-b566-1a4884a992e4')

        __delete_all(group.documents)
        __delete_all(group.trash)


def create_document(session, title='Underwater basket weaving'):
    return __create(session.documents, title)


def create_group_document(session, title='Underwater basket weaving'):
    return __create(session.groups.get('164d48fb-2343-332d-b566-1a4884a992e4').documents, title)


def __create(doc_resource, title):
    return doc_resource.create(title,
                               'journal',
                               authors=[Person.create('Piers', 'Bursill-Hall')],
                               source='Journal of Submarine Bambrology',
                               year=2014,
                               abstract='The wonders of creating exotic baskets in an underwater environment',
                               identifiers={'doi': 'doi123'},
                               keywords=['bambrology', 'submarine'],
                               pages='1-6',
                               volume='loud',
                               issue='73',
                               websites=['http://example.com/foo', 'http://example.com/bar'],
                               month=11,
                               publisher='Elsevier',
                               day=14,
                               city='Scunthorpe',
                               edition='First',
                               institution='University of Cambridge',
                               series='World Series',
                               chapter='99',
                               revision='2',
                               editors=[Person.create('John', 'Smith')],
                               accessed=arrow.get(2014, 9, 3),
                               read=False,
                               starred=True,
                               authored=False,
                               confirmed=True,
                               tags=['baskety', 'wet'])


def assert_core_document(doc):
    assert doc.id
    assert doc.title == 'Underwater basket weaving'
    assert doc.type == 'journal'
    assert doc.source == 'Journal of Submarine Bambrology'
    assert doc.year == 2014
    assert doc.abstract == 'The wonders of creating exotic baskets in an underwater environment'
    assert doc.identifiers['doi'] == 'doi123'
    assert doc.keywords == ['bambrology', 'submarine']
    assert doc.created
    assert doc.last_modified

    assert len(doc.authors) == 1
    assert doc.authors[0].first_name == 'Piers'
    assert doc.authors[0].last_name == 'Bursill-Hall'


def assert_bib_document(doc):
    assert doc.pages == '1-6'
    assert doc.volume == 'loud'
    assert doc.issue == '73'
    assert doc.websites == ['http://example.com/foo', 'http://example.com/bar']
    assert doc.month == 11
    assert doc.publisher == 'Elsevier'
    assert doc.day == 14
    assert doc.city == 'Scunthorpe'
    assert doc.edition == 'First'
    assert doc.institution == 'University of Cambridge'
    assert doc.series == 'World Series'
    assert doc.chapter == '99'
    assert doc.revision == '2'
    assert doc.accessed == arrow.get(2014, 9, 3)

    assert len(doc.editors) == 1
    assert doc.editors[0].first_name == 'John'
    assert doc.editors[0].last_name == 'Smith'


def assert_client_document(doc):
    assert not doc.read
    assert doc.starred
    assert not doc.authored
    assert doc.confirmed
    assert not doc.hidden


def assert_tags_document(doc):
    assert doc.tags == ['baskety', 'wet']


def assert_all_document(doc):
    assert_core_document(doc)
    assert_bib_document(doc)
    assert_client_document(doc)
    assert_tags_document(doc)
